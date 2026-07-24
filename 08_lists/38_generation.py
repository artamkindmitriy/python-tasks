N = int(input("Введите длину списка: "))

result = []

for index in range(1, N):
    if index % 2 == 0 or index == 0:
        result.append(1)
    else:
        result.append(index % 5)

print(f"Результат: {result}")