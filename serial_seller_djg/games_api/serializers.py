from rest_framework import serializers
from .models import SalesGames

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesGames
        fields = ('id','platform', 'link', 'img', 'title', 'original_price', 'discount_rate', 'discount_price', 'original_price_usd', 'discount_price_usd')
