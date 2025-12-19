from django.contrib import admin
from .models import Thread, ThreadRecommend, Comment, CommentRecommend

# Register your models here.
admin.site.register(Thread)
admin.site.register(ThreadRecommend)
admin.site.register(Comment)
admin.site.register(CommentRecommend)