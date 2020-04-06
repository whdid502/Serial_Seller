from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GameSerializer
from .models import SalesGames
#
# class GameViewSet(viewsets.ModelViewSet):
#     queryset = SalesGames.objects.all()
#     serializer_class = GameSerializer

from django_filters.rest_framework import DjangoFilterBackend

class UserFilterViewSet(viewsets.GenericViewSet):
    queryset = SalesGames.objects.all()
    serializer_class = GameSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('platform',)

    def list(self, request, *args, **kwargs):
        # data = super().list(request, args, kwargs)
        queryset = self.filter_queryset(self.get_queryset())

# Create your views here.
