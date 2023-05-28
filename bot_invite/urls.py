from django.urls import path
from .views import discord_link

urlpatterns = [
    path('discord/', discord_link, name='discord_link'),
]
