from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GameSerializer
from .models import SalesGames

class GameViewSet(viewsets.ModelViewSet):
    queryset = SalesGames.objects.all()
    serializer_class = GameSerializer
# Create your views here.
