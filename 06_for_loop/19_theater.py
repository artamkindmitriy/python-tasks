n = int(input("Введите число: "))
summ = 0

for i in range(1, n + 1, 5):
    summ += i
    print(f"Номер стула: {i}")
print(f"Сумма {summ}")