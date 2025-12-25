from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('get_threads/', views.get_threads),
    path('get_user_threads/', views.get_user_threads),
    path('get_thread/<int:thread_pk>/', views.get_thread),
    path('like_thread/<int:thread_pk>/', views.like_thread),
]
