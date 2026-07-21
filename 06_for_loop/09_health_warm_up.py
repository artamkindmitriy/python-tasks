start = int(input("Во сколько ты начал работать? "))

activity_minutes = 0
work_hours = 20 - start
for hour in range(start, 20):
    print(f"Сейчас {hour} часов")
    fit_minutes = int(input("Сколько минут разминки сделал? "))
    activity_minutes += fit_minutes
    if activity_minutes >= 45:
        print("Цель достигнута!")
        break

print(f"Общее кол-во часов проведенной за работой {work_hours}")
print(f"Кол-во минут разминки {activity_minutes}")