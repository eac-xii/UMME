from django.db import models
from django.conf import settings
from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator
)

spotify_id_validator = RegexValidator(
    regex=r'^[A-Za-z0-9]{22}$',
    message='Spotify ID must be exactly 22 characters.'
)

float_scope_validator = [
    MinValueValidator(0.0),
    MaxValueValidator(1.0)
]

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Artist(TimeStampedModel, models.Model):
    spotify_id = models.CharField(
        max_length=22,
        validators=[spotify_id_validator],
        unique=True
    )
    name = models.CharField(
        max_length=100
    )
    popularity = models.PositiveSmallIntegerField(null=True)
    image = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-popularity']


class Track(TimeStampedModel, models.Model):
    artists = models.ManyToManyField(
        Artist,
        related_name="tracks"
    )
    spotify_id = models.CharField(
        max_length=22,
        validators=[spotify_id_validator],
        unique=True
    )
    name = models.CharField(
        max_length=255
    )
    popularity = models.PositiveSmallIntegerField(null=True)
    image = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )
    release_date = models.DateField(null=True, blank=True)
    duration_ms = models.PositiveIntegerField()

    class Meta:
        ordering = ['-popularity']

class AudioFeatures(TimeStampedModel, models.Model):
    track = models.OneToOneField(
        Track,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="audio_features"
    )
    acousticness = models.FloatField(
        validators=float_scope_validator,
        null=True
    )
    danceability = models.FloatField(
        validators=float_scope_validator,
        null=True
    )
    energy = models.FloatField(
        validators=float_scope_validator,
        null=True
    )
    instrumentalness = models.FloatField(
        validators=float_scope_validator,
        null=True
    )
    KEY_CHOICES = [
        (-1, "unknown"),
        (0, "C"), (1, "C♯/D♭"), (2, "D"), (3, "D♯/E♭"),
        (4, "E"), (5, "F"), (6, "F♯/G♭"), (7, "G"),
        (8, "G♯/A♭"), (9, "A"), (10, "A♯/B♭"), (11, "B")
    ]
    key = models.SmallIntegerField(
        choices=KEY_CHOICES,
        null=True,
    )
    liveness = models.FloatField(
        validators=float_scope_validator,
        null=True
    )
    loudness = models.FloatField(
        validators=[
            MinValueValidator(-60.0),
            MaxValueValidator(0.0)
        ],
        null=True
    )
    mode = models.BooleanField(
        null=True,
        help_text="True=major, False=minor"
    )
    speechiness = models.FloatField(
        validators=float_scope_validator,
        null=True
    )
    tempo = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(300.0)
        ],
        null=True
    )
    valence = models.FloatField(
        validators=float_scope_validator,
        null=True
    )

class Playlist(TimeStampedModel, models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="playlists"
    )
    name = models.CharField(max_length=100)
    tracks = models.ManyToManyField(
        Track,
        through="PlaylistTrack",
        related_name="playlists",
    )
    is_public = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "name")


class PlaylistTrack(TimeStampedModel, models.Model):
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE
    )
    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.CASCADE
    )
    order_index = models.PositiveIntegerField()

    class Meta:
        ordering = ["order_index"]
