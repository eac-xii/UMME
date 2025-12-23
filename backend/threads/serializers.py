from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth import get_user_model
from .models import Thread
from musics.models import Artist, Track

User = get_user_model()

class ThreadListSerializer(serializers.ModelSerializer):
    class CustomUserDetailsSerializer(UserDetailsSerializer):
        is_spotify = serializers.SerializerMethodField()

        class Meta(UserDetailsSerializer.Meta):
            fields = UserDetailsSerializer.Meta.fields + ("is_spotify",)

        def get_is_spotify(self, user):
            return hasattr(user, "spotify")
            
    class TrackDetailSerializer(serializers.ModelSerializer):
        class ArtistListSerializer(serializers.ModelSerializer):
            class Meta:
                model = Artist
                fields = "__all__"
        
        artists = ArtistListSerializer(read_only=True, many=True)
        class Meta:
            model = Track
            fields = "__all__"
        
    user = CustomUserDetailsSerializer(read_only=True)
    track = TrackDetailSerializer(read_only=True)

    class Meta:
        model = Thread
        fields = "__all__"