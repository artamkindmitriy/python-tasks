n = int(input("До какого числа выводить квадраты: "))
for i in range(1, n // 2 + n % 2 + 1):
    odd_number = i * 2 - 1
    print("Число:", odd_number, "Квадрат числа:", odd_number ** 2)