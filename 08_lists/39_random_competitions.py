import random

first_team = [round(random.uniform(5, 10), 2) for number in range(1, 21)]
second_team = [round(random.uniform(5, 10), 2) for number in range(1, 21)]
win_team = []

for player_1, player_2 in zip(first_team, second_team):
    if player_1 > player_2:
        win_team.append(round(player_1, 2))
    else:
        win_team.append(round(player_2, 2))

print(f"Первая команда: {first_team}")
print(f"Вторая команда: {second_team}")
print(f"Победители тура: {win_team}")