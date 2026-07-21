count = 0
for i in range(1, 11):
    number = int(input("Введите номер человека: "))
    if number % 2 == 0 and number > 0:
        count += 1
print(f"Количество корректных номеров (чётных и положительных): {count}")