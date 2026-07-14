import math

first_weight = float(input("Введите первый вес: "))
second_weight = float(input("Введите вторый вес: "))

if math.isclose(first_weight + second_weight, 1, abs_tol=1e-5):
    print("Сумма равна 1")
else:
    print("Ошибка нормализации")