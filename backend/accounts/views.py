from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Profile, UserFeatures
from musics.models import Playlist

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