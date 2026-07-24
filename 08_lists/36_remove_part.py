import random

N = 10
numbers = [random.randint(1, 100) for _ in range(N)]
print("Исходный список:", numbers)

A = random.randint(0, N - 2)
B = random.randint(A + 1, N - 1)
print(f"A = {A}, B = {B}")

del numbers[A:B + 1]

print("Список после удаления:", numbers)