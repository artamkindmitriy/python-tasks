dogs = []

n = int(input("Кол-во чисел в списке: "))

for i in range(n):
    score = int(input("Введите очко: "))
    dogs.append(score)

min_score = min(dogs)
max_score = max(dogs)

print(f"Минимальное очко: {min_score}")
print(f"Максимальное очко: {max_score}")