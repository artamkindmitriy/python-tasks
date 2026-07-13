from typing import List

def calculate_area(width: float, height: float) -> float:
    return width * height

w = float(input("Введите ширину: "))
h = float(input("Введите высоту: "))

area = calculate_area(w, h)
print(f"Площадь: {area}")