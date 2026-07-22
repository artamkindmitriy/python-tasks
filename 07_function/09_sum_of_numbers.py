def summa_n(n):
    count = 0
    for i in range(1, n + 1):
        count += i
    print(f"Сумма чисел от 1 до {n} равна {count}")

n = int(input("Введите число: "))
summa_n(n)