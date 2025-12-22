from rest_framework import serializers
from .models import Artist, Track, PlaylistTrack

class ArtistNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("spotify_id", "name")

class TrackArtistSerializer(serializers.ModelSerializer):
    artists = ArtistNameSerializer(read_only=True, many=True)
    class Meta:
        model = Track
        fields = ("artists", "spotify_id", "name", "image", "duration_ms")

class PlaylistTracksSerializer(serializers.ModelSerializer):
    track = TrackArtistSerializer(read_only=True)
    class Meta:
        model = PlaylistTrack
        fields = ("track",)