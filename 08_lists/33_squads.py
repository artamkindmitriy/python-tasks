import random

damage_first_team = [random.randint(50, 80) for damage in range(1, 11)]
damage_second_team = [random.randint(30, 60) for damage in range(1, 11)]
third_team = []

print(f"Урон первого отряда: {damage_first_team}")
print(f"Урон второго отряда: {damage_second_team}")

for damage in range(10):
    if (damage_first_team[damage] + damage_second_team[damage]) > 100:
        third_team.append("Погиб")
    else:
        third_team.append("Выжил")

print(third_team)