goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print(f"Текущий ассортимент: {goods}")

fruit_name = input("Новый фрукт: ")
price = int(input("Цена: "))

goods.append([fruit_name, price])
print(f"Новый ассортимен: {goods}")

for item in goods:
    item[1] = round(item[1] * 1.08, 2)

print(f"Новый ассортимент с увел. ценой: {goods}")