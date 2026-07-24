n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))

print(f"Значит, выбывает каждый {k}-й человек")

circle = list(range(1, n + 1))
current_index = 0

while len(circle) > 1:
    print(f"\nТекущий круг людей: {circle}")
    print(f"Начало счёта с номера {circle[current_index]}")

    eliminated_index = (current_index + k - 1) % len(circle)
    eliminated_person = circle[eliminated_index]

    print(f"Выбывает человек под номером {eliminated_person}")

    circle.pop(eliminated_index)

    current_index = eliminated_index % len(circle)

print(f"\nОстался человек под номером {circle[0]}")