import graphene

import products.schema


class Query(products.schema.Query, graphene.ObjectType):
    """Inherit queries from all apps"""
    pass


class Mutation(products.schema.Mutation, graphene.ObjectType):
    """Inherit mutations from all apps"""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
