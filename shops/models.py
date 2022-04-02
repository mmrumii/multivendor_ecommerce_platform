from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ShopCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    datetime = models.DateTimeField('date')

    def __str__(self):
        return self.title
        
class Shop(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    datetime = models.DateTimeField('date')

    def __str__(self):
        return self.title

