from datetime import datetime
import graphene
import json

from data import get_product, get_all_products


class Product(graphene.ObjectType):
    """A Product has a title, price and inventory_count"""
    title = graphene.String()
    price = graphene.Float()
    inventory_count = graphene.Int()


class Query(graphene.ObjectType):
    product = graphene.Field(Product)
    all_products = graphene.List(Product)

    def resolve_product(self, info, title):
        return get_product(title)

    def resolve_all_products(self, info, is_available=False):
        return resolve_all_products(is_available)
