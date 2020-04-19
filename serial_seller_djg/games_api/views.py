from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import GameSerializer
from .models import SalesGames
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import GamePageNumberPagination
#
class GameViewSet(viewsets.ModelViewSet):
    queryset = SalesGames.objects.all()
    serializer_class = GameSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ['platform']
    ordering_fields = ['discount_price', 'discount_rate']
    pagination_class = GamePageNumberPagination
    # page_size = 16
    # page_query_param = 'page_size'
    # pagination_class = StandardResultsSetPagination

class IndexViewSet(viewsets.ModelViewSet):
    queryset = SalesGames.objects.all()
    serializer_class = GameSerializer

