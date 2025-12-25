from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)

float_scope_validator = [
    MinValueValidator(0.0),
    MaxValueValidator(1.0)
]

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


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
        unique=False,
        blank=False
    )

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=30,
        unique=False,
        blank=False
    )

    followings = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers'
    )

    created_at = models.DateTimeField(
        verbose_name="Date Joined",
        auto_now_add=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["last_name", "first_name"]

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.username

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
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="user"
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