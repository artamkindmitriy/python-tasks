n = int(input("Кол-во чисел в списке: "))
list_numbers = []

for i in range(1, n + 1):
    number = int(input(f"Введите {i} число: "))
    list_numbers.append(number)

divider = int(input("Введите делитель: "))
count = 0

for index, number in enumerate(list_numbers):
    if number % divider == 0:
        print(f"Индекс числа {number}: {index}")
        count += index

print(f"Сумма индексов: {count}")