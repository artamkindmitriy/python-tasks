number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

summ = 0
for i in range(number1, number2 + 1):
    summ += i
print(f"Сумма чисел от {number1} до {number2} равна {summ}")