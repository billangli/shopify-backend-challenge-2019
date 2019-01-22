from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    """Create a type for users to sign in and make API calls"""
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    """Queries for UserType"""
    users = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_users(self, info):
        """Return the list of all the users"""
        return get_user_model().objects.all()

    def resolve_me(self, info):
        """Return the user if the user is logged in, raise error otherwise"""
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in :O")

        return user


class CreateUser(graphene.Mutation):
    """A mutation for creating a user"""
    user = graphene.Field(UserType)

    class Arguments:
        """Arguments for creating a user"""
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        """Create the user and return it to the client"""
        user = get_user_model() (
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    """A class for listing the mutations"""
    create_user = CreateUser.Field()
