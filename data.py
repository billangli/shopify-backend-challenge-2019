from schema import Product


product_data = []

def setup():
    """Create example data"""
    global product_data

    towel = Product(
        title = 'towel',
        price = 4.99,
        inventory_count = 5
    )

    toothbrush = Product(
        title = 'toothbrush',
        price = 5.99,
        inventory_count = 50
    )


    toothpaste = Product(
        title = 'toothpaste',
        price = 10,
        inventory_count = 2
    )

    product_data = [towel, toothbrush, toothpaste]


def get_product(title):
    """Return the product by title, return None if not found"""
    for product in product_data:
        if product.title == title:
            return product

    return None


def get_all_products(is_available):
    """
    Return the entire list of products, if is_available is True, then
    return a list of products that are in stock
    """
    if is_available:
        result = []
        for product in all_products:
            if product.inventory_count > 0:
                result.append(product)
        return result
    else:
        return all_products
