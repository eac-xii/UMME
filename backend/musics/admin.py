from django.contrib import admin
from .models import Artist, Track, AudioFeatures, Playlist, PlaylistTrack

# Register your models here.
admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(AudioFeatures)
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)