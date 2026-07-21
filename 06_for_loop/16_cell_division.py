hours = int(input("Количество часов: "))
cell = 1

for i in range(hours // 3 + 1):
    cell += 2
    print("Прошло часов:", i * 3)
    print("Количество клеток:", cell)
    print("Осталось часов:", hours - i * 3)
print("Наблюдение завершено")