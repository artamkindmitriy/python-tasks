temperature = int(input("Сколько градусов на улице? "))
meters = 0
while temperature > 15:
    meters += 20
    temperature -= 2
    if temperature <= 15:
        break
    meters += 10
print("Пройдено метров:", meters)