from django.urls import path
from . import views

urlpatterns = [
    path('spotify/callback/', views.spotify_callback),
    path('spotify/playback_token/', views.spotify_playback_token),
    path('spotify/transfer_playback/', views.spotify_transfer_playback),
    path('spotify/play/', views.spotify_play),
    path('spotify/search/', views.spotify_search),
]
