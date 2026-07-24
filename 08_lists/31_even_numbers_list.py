a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

numbers = []
for i in range(a, b + 1):
    if i % 2 == 0:
        numbers.append(i)

print(numbers)