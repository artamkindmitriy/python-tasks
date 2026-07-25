prices = {'молоко': 80, 'хлеб': 40, 'сыр': 250, 'яйца': 120}
cart = {'молоко': 2, 'сыр': 1, 'кофе': 1}

total_price = 0

for product, quantity in cart.items():
    price = prices.get(product)
    if price is not None:
        cost = price * quantity
        total_price += cost
        print(f"Товар{product}:{quantity} шт. *{price} руб. ={cost} руб.")
    else:
        print(f"Товар{product} не найден, цена 0")

print(f"\nИтоговая цена покупки:{total_price} рублей")