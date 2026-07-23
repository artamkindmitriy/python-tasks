main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

first_company = [0, 0, 0]

second_company = [1, 0, 0, 1, 1]

third_company = [1, 1, 1, 0, 1]

count = 0

combined = main + first_company + second_company + third_company
print(f"Общий список задач: {combined}")

for i in combined:
    if i == 0:
        count += 1
print(f"Кол-во невыполненных задач: {count}")