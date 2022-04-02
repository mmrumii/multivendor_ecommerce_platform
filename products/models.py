from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from shops.models import Shop

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    datetime = models.DateTimeField('date')

    def __str__(self):
        return self.title
        
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    owner = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    datetime = models.DateTimeField('date')

    def __str__(self):
        return self.title

