N = int(input("Количество роликов: "))

size_roll = []
size_human = []

count = 0

for sizes in range(1, N + 1):
    size = int(input(f"Размер пары {sizes}: "))
    size_roll.append(size)

K = int(input("Количество людей: "))

for sizes in range(1, K + 1):
    size = int(input(f"Размер ноги человека {sizes}: "))
    size_human.append(size)

size_roll.sort()
size_human.sort()

for human_size in size_human:
    for roll_size in size_roll:
        if roll_size >= human_size:
            count += 1
            size_roll.remove(roll_size)
            break

print(f"Наибольшее количество людей, которые могут взять ролики: {count}")