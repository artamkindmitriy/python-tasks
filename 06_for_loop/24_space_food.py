months = 0
print("Информация о запасах гречки:")
for i in range(100, 0, -4):
    months += 1
    print(f"Через {months} месяц: {i} кг гречки в запасе")

    if i == 0:
        print("Запас гречки закончился")
        break