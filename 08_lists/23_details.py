shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_detail = input("Название детали: ")

count = 0
total_price = 0

for item in shop:
    if item[0].lower() == name_detail.lower():
        count += 1
        total_price += item[1]

if count > 0:
    print(f"Количество деталей: {count}")
    print(f"Общая стоимость: {total_price}")
else:
    print("Такого товара нет в магазине")