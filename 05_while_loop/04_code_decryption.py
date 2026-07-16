number = int(input("Введите последовательность чисел: "))
summ = 0
while number != 0:
    last_num = number % 10
    if last_num == 5:
        print("Обнаружен разрыв!")
        break
    summ += last_num
    number //= 10
print(summ)