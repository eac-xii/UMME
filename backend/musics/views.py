import os
from dotenv import load_dotenv
load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

import requests, json, base64
from datetime import timedelta
from django.utils import timezone

from django.shortcuts import redirect, get_object_or_404

from accounts.models import SpotifyAccount
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Playlist

User = get_user_model()

#region Token Handlers
def refresh_spotify_token(spotify):
    if not spotify.refresh_token:
        raise ValueError("No refresh_token sotred")
    
    token_url = "https://accounts.spotify.com/api/token"

    auth_header = base64.b64encode(
        f"{client_id}:{client_secret}".encode()
    ).decode()

    response = requests.post(
        token_url,
        data={
            "grant_type": "refresh_token",
            "refresh_token": spotify.refresh_token,
        },
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    spotify.access_token = data["access_token"]

    if "refresh_token" in data:
        spotify.refresh_token = data["refresh_token"]

    spotify.expires_at = timezone.now() + timedelta(
        seconds=data["expires_in"]
    )

    spotify.save(update_fields=[
        "access_token",
        "expires_at",
        "refresh_token",
        "updated_at"
    ])

    return spotify.access_token

def ensure_valid_token(spotify, buffer_seconds=30):
    if spotify.expires_at <= timezone.now() + timedelta(seconds=buffer_seconds):
        refresh_spotify_token(spotify)

    return spotify.access_token
#endregion

# Create your views here.
@api_view(["GET"])
def spotify_callback(request):
    if request.method == "GET":
        code = request.GET.get("code")
        state = request.GET.get("state")

        data = json.loads(base64.b64decode(state).decode())
        user_id = data["user_id"]

        user = get_object_or_404(User, id=user_id)

        token_response = requests.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": redirect_uri,
            },
            headers={
                "Authorization": "Basic "
                    + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )

        tokens = token_response.json()

        SpotifyAccount.objects.update_or_create(
            user=user,
            defaults={
                "access_token": tokens["access_token"],
                "refresh_token": tokens["refresh_token"],
                "expires_at": timezone.now() + timedelta(seconds=tokens["expires_in"]),
                "scope": tokens["scope"]
            }
        )

        return redirect("http://localhost:5173/")

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def spotify_playback_token(request):
    if request.method == "GET":
        spotify = request.user.spotify

        if "streaming" not in spotify.scope:
            return Response(
                {"detail": "Spotify streaming 권한 없음"},
                status=403
            )

        ensure_valid_token(spotify)
        
        return Response({ "access_token": spotify.access_token })

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def spotify_transfer_playback(request):
    if request.method == "PUT":
        spotify = request.user.spotify
        ensure_valid_token(spotify)

        requests.put(
            "https://api.spotify.com/v1/me/player",
            json={
                "device_ids": [request.data["device_id"]],
                "play": True
            },
            headers={
                "Authorization": f"Bearer {spotify.access_token}"
            }
        )

        return Response(status=204)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def spotify_play(request):
    if request.method == "PUT":
        spotify = request.user.spotify
        ensure_valid_token(spotify)

        device_id = request.data.get("device_id")

        requests.put(
            "https://api.spotify.com/v1/me/player/play",
            params={
                "device_id": device_id
            },
            json={
                "uris": request.data.get("uris")
            },
            headers={
                "Authorization": f"Bearer {spotify.access_token}"
            },
            timeout=5
        )

        return Response(status=204)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)
spcc = spotipy.Spotify(auth_manager=auth_manager)

from rapidfuzz import fuzz
from pprint import pprint
@api_view(["GET"])
def spotify_search(request):
    if request.method == "GET":
        query = request.GET.get("query")
        response = spcc.search(query, limit=5, offset=0, type='artist,track', market=None)
        artists = response["artists"]["items"]
        tracks = response["tracks"]["items"]

        combined_results = []

        for artist in artists:
            similarity = fuzz.partial_ratio(query, artist["name"])
            score = similarity * 1.15 + artist["popularity"] * 1.05
            combined_results.append({
                'type': 'artist',
                'data': artist,
                'score': score
            })

        for track in tracks:
            similarity = fuzz.partial_ratio(query, track["name"])
            score = similarity * 1.0 + track["popularity"] * 1.2
            combined_results.append({
                'type': 'track',
                'data': track,
                'score': score
            })

        sorted_results = sorted(combined_results, key=lambda x: x['score'], reverse=True)
    return Response(sorted_results)

@api_view(["GET"])
def spotify_search_artist_tracks(request):
    if request.method == "GET":
        artist_id = request.GET.get("artistId")
        response = spcc.artist_top_tracks(artist_id=artist_id)
        response = [{"data": track, "type": "track"} for track in response["tracks"]]
        return Response(response)
    

from datetime import date
from .models import Artist, Track, AudioFeatures, PlaylistTrack
from django.db.models import Max
reccobeats_base_url = "https://api.reccobeats.com/v1"

def parse_spotify_release_date(date_str: str) -> date:
    if not date_str:
        return None
    
    if len(date_str) == 4:
        return date(int(date_str), 1, 1)
    elif len(date_str) == 7:
        year, month = map(int, date_str.split("-"))
        return date(year, month, 1)
    else:
        return date.fromisoformat(date_str)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_track_to_playlist(request):
    if request.method == "POST":
        data = request.data["track"]
        artists = data["artists"]
        spotify_ids = []
        for artist in artists:
            detail = spcc.artist(artist["id"])
            spotify_ids.append(detail["id"])
            newArtist, _ = Artist.objects.get_or_create(
                spotify_id=detail["id"],
                name=detail["name"],
                popularity=detail["popularity"],
                image=detail["images"][0]["url"] if detail["images"] else ''
            )
        artists = Artist.objects.filter(spotify_id__in=spotify_ids)
        newTrack, _ = Track.objects.get_or_create(
            spotify_id=data["id"],
            name=data["name"],
            popularity=data["popularity"],
            image=data["album"]["images"][0]["url"] if data["album"]["images"] else '',
            release_date=parse_spotify_release_date(data["album"]["release_date"]),
            duration_ms=data["duration_ms"]
        )
        newTrack.artists.set(artists)

        headers = {
            "Accept": "application/json"
        }
        item = requests.request(
            "GET",
            f"{reccobeats_base_url}/audio-features",
            headers=headers,
            params={
                "ids": data["id"]
            }
        ).json()["content"]

        if item:
            item = item[0]
            track = Track.objects.get(spotify_id=data["id"])
            audiofeatures, _ = AudioFeatures.objects.get_or_create(
                track=track,
                acousticness=item["acousticness"],
                danceability=item["danceability"],
                energy=item["energy"],
                instrumentalness=item["instrumentalness"],
                key=item["key"],
                liveness=item["liveness"],
                loudness=item["loudness"],
                mode=item["mode"],
                speechiness=item["speechiness"],
                tempo=item["tempo"],
                valence=item["valence"]
            )

        targetPlaylist = Playlist.objects.get(user=request.user)

        max_index = PlaylistTrack.objects.filter(playlist=targetPlaylist).aggregate(Max('order_index'))['order_index__max']

        next_index = (max_index + 1) if max_index is not None else 0

        playlistTrack, _ = PlaylistTrack.objects.get_or_create(
            track=newTrack,
            playlist=targetPlaylist,
            order_index=next_index
        )
        return Response(status=201)

from .serializers import PlaylistTracksSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_playlist_items(request):
    if request.method == "GET":
        user = request.user
        playlist = Playlist.objects.get(user=user)
        playlist_track = PlaylistTrack.objects.filter(playlist=playlist)
        serializer = PlaylistTracksSerializer(playlist_track, many=True)
        return Response(serializer.data)