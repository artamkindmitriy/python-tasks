def avg(a, b):
    print("Среднее:", round((a + b) / 2, 2))

a = int(input("Введите левую границу: "))
b = int(input("Введите правую границу: "))

if a > b:
    a, b = b, a

avg(a, b)