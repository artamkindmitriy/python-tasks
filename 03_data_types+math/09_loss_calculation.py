import math

p = float(input("Введите вероятность (от 0 до 1): "))

if p > 0:
    result = round(-math.log(p), 4)
    print(f"Потеря: {result}")
else:
    print("Ошибка: вероятность должна быть больше 0")