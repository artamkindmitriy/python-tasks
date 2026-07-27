import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3,
          16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12,
          9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums_1_set = set(nums_1)
nums_2_set = set(nums_2)

print(f"1-е множество:{nums_1_set}")
print(f"2-е множество:{nums_2_set}")

print()

min_val_1 = min(nums_1_set)
nums_1_set.remove(min_val_1)

min_val_2 = min(nums_2_set)
nums_2_set.remove(min_val_2)

print(f"Минимальный элемент 1-го множества:{min_val_1}")
print(f"Минимальный элемент 2-го множества:{min_val_2}")

print()

add_random_el_1 = random.randint(100, 200)
nums_1_set.add(add_random_el_1)

add_random_el_2 = random.randint(100, 200)
nums_2_set.add(add_random_el_2)

print(f"Случайное число для 1-го множества:{add_random_el_1}")
print(f"Случайное число для 2-го множества:{add_random_el_2}")

print()

print(f"Объединение множеств:{nums_1_set | nums_2_set}")
print(f"Пересечение множеств:{nums_1_set & nums_2_set}")
print(f"Элементы, входящие в nums_2, но не входящие в nums_1:{nums_2_set - nums_1_set}")