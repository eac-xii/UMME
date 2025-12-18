from django.contrib import admin
from .models import Artist, Track, AudioFeatures, Playlist, PlaylistTrack

# Register your models here.
admin.site.register(Artist, Track, AudioFeatures, Playlist, PlaylistTrack)