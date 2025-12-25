from django.urls import path
from . import views

urlpatterns = [
    path('spotify/callback/', views.spotify_callback),
    path('spotify/playback_token/', views.spotify_playback_token),
    path('spotify/transfer_playback/', views.spotify_transfer_playback),
    path('spotify/play/', views.spotify_play),
    path('spotify/search/', views.spotify_search),
    path('spotify/search_artist_tracks/', views.spotify_search_artist_tracks),
    path('spotify/add_track_to_playlist/', views.add_track_to_playlist),
    path('get_playlist_items/', views.get_playlist_items),
    path('get_audiofeatures/<int:track_id>/', views.get_audiofeatures),
]
