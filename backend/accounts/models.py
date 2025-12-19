from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from musics.models import Track
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)

float_scope_validator = [
    MinValueValidator(0.0),
    MaxValueValidator(1.0)
]

class UserManager(BaseUserManager):
    def create_user(self, email, username, last_name, first_name, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
        )

        user.is_spotify = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, last_name, first_name, nickname, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username=username,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
            password=password,
        )
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    username = models.CharField(
        verbose_name="Username",
        max_length=30,
        unique=False
    )

    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=30,
        unique=False
    )

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=30,
        unique=False
    )

    nickname = models.CharField(
        verbose_name="Nickname",
        max_length=30,
        unique=True
    )

    created_at = models.DateTimeField(
        verbose_name="Date Joined",
        auto_now_add=True
    )

    is_spotify = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname", "last_name", "first_name"]

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.nickname

class SpotifyAccount(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="spotify"
    )
    access_token = models.TextField()
    refresh_token = models.TextField()
    expires_at = models.DateTimeField()
    scope = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following"
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followers"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"],
                name="unique_follow"
            ),
            models.CheckConstraint(
                condition=~models.Q(follower=models.F("following")),
                name="prevent_self_follow"
            ),
        ]

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    content = models.CharField(max_length=255, blank=True)

    def profile_image_path(instance, filename):
        return f"profiles/{instance.user.id}/{filename}"

    image = models.ImageField(
        upload_to=profile_image_path,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.nickname}'s profile"
    
class UserFeatures(models.Model):
    user = models.OneToOneField(
        Track,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="user"
    )
    acousticness = models.FloatField(
        validators=float_scope_validator
    )
    danceability = models.FloatField(
        validators=float_scope_validator
    )
    energy = models.FloatField(
        validators=float_scope_validator
    )
    instrumentalness = models.FloatField(
        validators=float_scope_validator
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
        validators=float_scope_validator
    )
    loudness = models.FloatField(
        validators=[
            MinValueValidator(-60.0),
            MaxValueValidator(0.0)
        ]
    )
    mode = models.BooleanField(
        null=True,
        help_text="True=major, False=minor"
    )
    speechiness = models.FloatField(
        validators=float_scope_validator
    )
    tempo = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(300.0)
        ]
    )
    valence = models.FloatField(
        validators=float_scope_validator
    )