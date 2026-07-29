with open("day_plan.txt", "w") as file:
    file.write("Пропылесосить\nПочитать книгу\nПокодить")

with open("day_plan.txt", "r") as f:
    print(f.read())