from django.shortcuts import render
from django.http import HttpResponse
from .models import Player

# Create your views here.
def index(request):
    return HttpResponse("Hello world welcome to my tournament page :)")
def details(request):
    players = Player.objects.all()
    players= [
        f"{player.first_name} {player.last_name}" for player in players
    ]
    return HttpResponse(players)