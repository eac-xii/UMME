import os 
from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv("VUE_BASE_URL")

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Thread
from musics.models import Track, AudioFeatures

from .serializers import ThreadSerializer

# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def create(request):
    if request.method == "GET":
        return redirect(f"{base_url}")
    elif request.method == "POST":
        track_id = request.data["track_id"]

        user = request.user
        track = Track.objects.get(spotify_id=track_id)
        content = request.data["content"]
        thread = Thread.objects.create(
            user=user,
            track=track,
            content=content
        )
        return Response(status=201)
    
@api_view(["GET"])
def get_threads(request):
    if request.method == "GET":
        query_filter = request.GET.get("filter")
        if query_filter == "all":
            threads = Thread.objects.all()
            serializer = ThreadSerializer(threads, many=True)
            return Response(serializer.data, status=200)

        else:
            return Response(status=204)
        
@api_view(["GET"])
def get_user_threads(request):
    if request.method == "GET":
        user = request.GET.get("userId")
        threads = Thread.objects.filter(user=user)
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data, status=200)

@api_view(["GET"])
def get_thread(request, thread_pk):
    if request.method == "GET":
        thread = get_object_or_404(Thread, pk=thread_pk)
        serializer = ThreadSerializer(thread)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def like_thread(request, thread_pk):
    if request.method == "PUT":
        thread = get_object_or_404(Thread, pk=thread_pk)
        if request.user in thread.like_threads.all():
            thread.like_threads.remove(request.user)
            is_liked = False
        else:
            thread.like_threads.add(request.user)
            is_liked = True
        return Response({"is_liked": is_liked}, status=status.HTTP_200_OK)
    