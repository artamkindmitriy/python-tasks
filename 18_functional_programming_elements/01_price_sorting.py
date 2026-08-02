catalog = [
    {"item": "Brake Pads", "price": 4500},
    {"item": "Oil Filter", "price": 1200},
    {"item": "Spark Plugs", "price": 2500},
    {"item": "Windshield Wipers", "price": 1800},
]

result = sorted(catalog, key=lambda item: item["price"], reverse=True)

for product in result:
    print(product)