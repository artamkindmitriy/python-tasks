get_up = int(input("Во сколько ты проснулся? "))
n_calories = int(input("Сколько калорий ты съедаешь за один приём? "))

total_liters = 0
total_calories = 0

for i in range(get_up, 23 + 1, 3):
    total_liters += 1
    total_calories += n_calories

print(f"За день ты выпил {total_liters} литров воды и съел {total_calories} калорий")