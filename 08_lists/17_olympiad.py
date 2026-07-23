n = int(input("Кол-во участников: "))
k = int(input("Кол-во человек в команде: "))

if n % k != 0:
    print(f"{n} участников невозможно поделить на команды по {k} человек")
else:
    teams = []
    for i in range(0, n, k):
        team = list(range(i + 1, i + k + 1))
        teams.append(team)

    print("Общий список команд:", teams)