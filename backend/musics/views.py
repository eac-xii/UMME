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
    spotify = request.user.spotify
    ensure_valid_token(spotify)

    device_id = request.data.get("device_id")

    requests.put(
        "https://api.spotify.com/v1/me/player/play",
        params={
            "device_id": device_id
        },
        json={
            "uris": request.data["uris"]
        },
        headers={
            "Authorization": f"Bearer {spotify.access_token}"
        },
        timeout=5
    )

    return Response(status=204)