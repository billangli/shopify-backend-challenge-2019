from django.db import models


class Product(models.Model):
    """A product has a title, price and inventory_count"""
    title = models.CharField(max_length=50)
    price = models.FloatField()
    inventory_count = models.IntegerField()
