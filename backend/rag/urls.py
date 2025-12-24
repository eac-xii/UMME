# rag/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.RagQueryView.as_view(), name='rag-query'),
]