from django.contrib import admin
from .models import Thread, ThreadRecommend, Comment, CommentRecommend

# Register your models here.
admin.site.register(Thread, ThreadRecommend, Comment, CommentRecommend)