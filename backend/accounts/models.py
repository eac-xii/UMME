from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, last_name, first_name, nickname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        if not last_name:
            raise ValueError("Users must have a last name")
        
        if not first_name:
            raise ValueError("Users must have a first name")

        user = self.model(
            email=self.normalize_email(email),
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
        )

        user.is_spotify = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, last_name, first_name, nickname, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
            password=password,
        )
        
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=30,
        unique=True
    )

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=30,
        unique=True
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
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname", "last_name", "first_name"]

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin