from datetime import datetime
import graphene
from graphene_django import DjangoObjectType
import json

from .models import Product


class ProductType(DjangoObjectType):
    class Meta:
        """A Product has a title, price and inventory_count"""
        model = Product


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()
