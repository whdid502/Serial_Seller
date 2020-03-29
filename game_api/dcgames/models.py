from django.db import models

# Create your models here.
class Games(models.Model):
    platform = models.CharField(max_length=10)
    link = models.CharField