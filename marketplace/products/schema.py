from datetime import datetime
import graphene
from graphene_django import DjangoObjectType
import json

from .models import Product


class ProductType(DjangoObjectType):
    class Meta:
        """A Product has a title, price and inventory_count"""
        model = Product


class Query(object):
    """Queries for ProductType"""
    product = graphene.Field(ProductType, title=graphene.String())
    all_products = graphene.List(ProductType, in_stock=graphene.Boolean())

    def resolve_product(self, info, **kwargs):
        """Get a single product by title"""
        title = kwargs.get('title')

        if title is not None:
            return Product.objects.get(title=title)

        return None

    def resolve_all_products(self, info, **kwargs):
        """Get all products, if in_stock is true, then only display items in stock"""
        in_stock = kwargs.get('in_stock')

        if in_stock is not None:
            if in_stock:
                return Product.objects.filter(inventory_count__gt=0)

        return Product.objects.all()


class CreateProduct(graphene.Mutation):
    """Mutation for the client to send data to API to create product"""
    id = graphene.ID()
    title = graphene.String()
    price = graphene.Float()
    inventory_count = graphene.Int()

    class Arguments:
        title = graphene.String()
        price = graphene.Float()
        inventory_count = graphene.Int()

    def mutate(self, info, title, price, inventory_count):
        product = Product(title=title, price=price, inventory_count=inventory_count)
        product.save()

        return CreateProduct(
            id=product.id,
            title=title,
            price=price,
            inventory_count=inventory_count,
        )


class PurchaseProduct(graphene.Mutation):
    """Mutation for a user to purchase a product by the name"""
    id = graphene.ID()
    success = graphene.Boolean()
    title = graphene.String()
    price = graphene.Float()
    inventory_count = graphene.Int()

    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        product = Product.objects.get(title=title)

        # Check how many items are left in inventory
        if product.inventory_count > 0:
            # Item purchased sucessfully
            product.inventory_count -= 1
            product.save()
            success = True
        else:
            # Item purchase failed
            success = False

        return PurchaseProduct(
            id=product.id,
            success=success,
            title=product.title,
            price=product.price,
            inventory_count=product.inventory_count,
        )


class Mutation(graphene.ObjectType):
    """A class for listing the mutations"""
    create_product = CreateProduct.Field()
    purchase_product = PurchaseProduct.Field()
