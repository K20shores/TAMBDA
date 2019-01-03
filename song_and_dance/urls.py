from django.urls import path
from django.shortcuts import render
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.song_and_dance, name='song_and_dance'),
    path('generate/', views.generate, name='generate'),
]