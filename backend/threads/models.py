from django.db import models
from django.conf import settings
from musics.models import Track

# Create your models here.
class Thread(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="threads"
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        related_name="threads"
    )
    content = models.TextField(max_length=660)
    like_threads = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
