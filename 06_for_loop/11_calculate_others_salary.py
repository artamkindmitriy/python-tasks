summ = 0
count = 0

for month in range(1, 13):
    salary = int(input("Введите зарплату сотрудника: "))
    summ += salary
    count += 1

print(f"Средняя зарплата за год: {summ / count}")