import graphene

import products.schema


class Query(products.schema.Query, graphene.ObjectType):
    """Inherit queries from all apps"""
    pass

schema = graphene.Schema(query=Query)
