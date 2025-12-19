from django.contrib import admin
from .models import ChatRoom, ChatUser, Message

# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(ChatUser)
admin.site.register(Message)