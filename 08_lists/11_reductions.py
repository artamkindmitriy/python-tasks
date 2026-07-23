salaries = []
count = 0

cwk = int(input("Кол-во сотрудников: "))

for person in range(1, cwk + 1):
    salary = int(input(f"Зарплата {person} сотрудника: "))
    if salary == 0:
        continue

    salaries.append(salary)
    count += 1

print(f"Осталось сотрудников: {count}")
print(f"Зарплаты: {salaries}")

print(f"Максимальная зп: {max(salaries)}")
print(f"Минимальная зп: {min(salaries)}")