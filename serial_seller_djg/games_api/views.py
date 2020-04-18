from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .serializers import GameSerializer
from .models import SalesGames
from django_filters.rest_framework import DjangoFilterBackend
#
class GameViewSet(viewsets.ModelViewSet):
    queryset = SalesGames.objects.all()
    serializer_class = GameSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ['platform']
    ordering_fields = ['discount_price', 'discount_rate']

