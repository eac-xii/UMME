from django.db import models
from django.conf import settings

# Create your models here.
class ChatRoom(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class ChatUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chat_users"
    )
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name="participants"
    )

    class Meta:
        unique_together = ("user", "room")

class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)