import math

def cylinder_calc(radius, height):
    s_side_cylinder = 2 * math.pi * radius * height
    s_full_cylinder = 2 * math.pi * radius * (height + radius)

    return s_side_cylinder, s_full_cylinder

radius = int(input("Введите радиус цилиндра: "))
height = int(input("Введите высоту цилиндра: "))

side, full = cylinder_calc(radius, height)

print(f"Площадь боковой поверхности цилиндра:{round(side, 2)}")
print(f"Площадь полной поверхности цилиндра:{round(full, 2)}")