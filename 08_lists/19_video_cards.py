count_cart = int(input("Количество видеокарт: "))

old_list_cart = []
new_list_cart = []

for n in range(1, count_cart + 1):
    cart = int(input(f"Видеокарта {n}: "))
    old_list_cart.append(cart)

print(f"Старый список видеокарт: {old_list_cart}")

max_val = max(old_list_cart)

new_list_cart = [p for p in old_list_cart if p != max_val]

print(f"Новый список видеокарт: {new_list_cart}")