from django.db import models

class Game(models.Model):
    platform = models.CharField(max_length=30)
    link = models.TextField()
    img = models.TextField()
    title = models.CharField(max_length=30)
    original_price = models.IntegerField()
    discount_rate = models.IntegerField()
    discount_price = models.IntegerField()
    original_price_usd = models.IntegerField()
    discount_price_usd = models.IntegerField()

    def __str__(self):
        return self.platform
# Create your models here.
