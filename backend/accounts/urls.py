from django.urls import path
from . import views

urlpatterns = [
    path('init_user_settings/', views.init_user_settings),
    path('get_profile/<int:user_pk>/', views.get_profile),
    path('get_playlist/<int:user_pk>/', views.get_playlist),
    path('update_profile/', views.update_profile),
    path('follow/<int:user_pk>/', views.follow),
]