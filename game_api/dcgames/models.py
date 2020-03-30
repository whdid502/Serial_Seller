from django.db import models

# Create your models here.
class Games(models.Model):
    platform = models.CharField(max_length=10)
    link = models.TextField()
    img = models.TextField()
    title = models.CharField(max_length=80)
    original_price = models.IntegerField()
    discount_rate = models.IntegerField()
    discount_price = models.IntegerField()
    original_price_usd = models.FloatField()
    discount_price_usd = models.FloatField()

    def __str__(self):
        return self.platform