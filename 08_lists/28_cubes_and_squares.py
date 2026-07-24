a = int(input("Левая граница: "))
b = int(input("Правая граница: "))

cubes = []
squares = []

for i_cubes in range(a, b + 1):
    cubes.append(i_cubes ** 3)

for i_squares in range(a, b + 1):
    squares.append(i_squares ** 2)

print(f"Список кубов чисел в диапозоне от {a} до {b}: {cubes}")
print(f"Список квадратов чисел в диапозоне от {a} до {b}: {squares}")