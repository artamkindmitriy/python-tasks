players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team_a_rest = []
team_b_training = []
team_c_travel = []

for team in players_dict.values():
    if team["team"] == "A" and team["status"] == "Rest":
        team_a_rest.append(team["name"])
    elif team["team"] == "B" and team["status"] == "Training":
        team_b_training.append(team["name"])
    elif team["team"] == "C" and team["status"] == "Travel":
        team_c_travel.append(team["name"])

print(f"Результат группы А:{team_a_rest}")
print(f"Результат группы B:{team_b_training}")
print(f"Результат группы C:{team_c_travel}")