from rest_framework import serializers
from .models import Games

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('id','platform','link','img', 'title', 'original_price', 'discount_rate', 'discount_price', 'original_price_usd', 'discount_price_usd') # 필드 설정