from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Profile, UserFeatures
from musics.models import Playlist, PlaylistTrack
from django.contrib.auth import get_user_model

from .serializers import ProfileSerializer
from musics.serializers import PlaylistTracksSerializer

from django.shortcuts import get_object_or_404, get_list_or_404

User = get_user_model()

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def init_user_settings(request):
    if request.method == "POST":
        profile, created = Profile.objects.get_or_create(
            user=request.user,
        )

        if created:
            print(f"[ACCOUNTS] | init_user_settings\n :: Profile created for {profile.user.username}.")
        else:
            print(f"[ACCOUNTS] | init_user_settings\n :: Profile for {profile.user.username} alreay exist.")            

        userfeatures, created = UserFeatures.objects.get_or_create(
            user=request.user,
        )

        if created:
            print(f"[ACCOUNTS] | init_user_settings\n :: UserFeatures created for {userfeatures.user.username}.")
        else:
            print(f"[ACCOUNTS] | init_user_settings\n :: UserFeatures for {userfeatures.user.username} alreay exist.")   
        
        playlist, created = Playlist.objects.get_or_create(
            user=request.user,
            name="My Playlist",
            is_public=True
        )

        if created:
            print(f"[ACCOUNTS] | init_user_settings\n :: Playlist created for {playlist.user.username}.")
        else:
            print(f"[ACCOUNTS] | init_user_settings\n :: Playlist for {playlist.user.username} alreay exist.")   

        return Response(
            data={"success": "User setting has been successfully initialized."},
            status=status.HTTP_201_CREATED
        )
    
@api_view(["GET"])
def get_profile(request, user_pk):
    if request.method == "GET":
        user = get_object_or_404(User, pk=user_pk)
        profile = get_object_or_404(Profile, user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_playlist(request, user_pk):
    if request.method == "GET":
        user = get_object_or_404(User, pk=user_pk)
        playlist = get_object_or_404(Playlist, user=user)
        tracks = get_list_or_404(PlaylistTrack, playlist=playlist)
        serializer = PlaylistTracksSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["PUT"])
def update_profile(request):
    if request.method == "PUT":
        profile = get_object_or_404(Profile, user=request.user.pk)
        serializer = ProfileSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            