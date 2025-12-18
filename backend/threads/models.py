from django.db import models
from django.conf import settings
from ..musics.models import Track

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
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ThreadRecommend(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recommended_threads"
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name="recommends"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "thread")


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


class CommentRecommend(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recommended_comments"
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="recommends"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "comment")
