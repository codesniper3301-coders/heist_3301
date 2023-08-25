from django.db import models
from django.contrib.auth.models import User  
# Create your models here.
class portfolio(models.Model):
    symbol=models.CharField(max_length=10,default='')
    price_bought=models.BigIntegerField(default=0)
    fraction_bought=models.FloatField(default=0.0)
    def __str__(self):
        return self.symbol

class buffer(models.Model):
    symbol=models.CharField(max_length=10,default='')
    price_bought=models.BigIntegerField(default=0)
    buffer=models.FloatField(default=0.0)
    def __str__(self):
        return self.symbol