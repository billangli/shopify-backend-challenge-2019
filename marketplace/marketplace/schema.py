import graphene
import graphql_jwt

import products.schema, users.schema


class Query(products.schema.Query, users.schema.Query, graphene.ObjectType):
    """Inherit queries from all apps"""
    pass


class Mutation(products.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    """Inherit mutations from all apps"""
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
