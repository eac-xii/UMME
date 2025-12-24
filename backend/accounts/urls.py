from django.urls import path
from . import views

urlpatterns = [
    path('init_user_settings/', views.init_user_settings),
]