import graphene


schema = graphene.Schema(query=Query)

result = schema.execute(
"""
{
    all_products {
        title
        price
    }
}
"""
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))
