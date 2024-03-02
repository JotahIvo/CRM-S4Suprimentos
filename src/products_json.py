import src.database as database


def products_json():
    products = database.select_all_products()
    products_json = []

    for product in products:
        products_json.append(
            {"id": product[0], "name": product[1], "description": product[2], "price": product[3]}
        )
    return products_json