new_task = input("Введите новую задачу: ")

with open("day_plan.txt", "a") as file:
    file.write(new_task + "\n")

with open("day_plan.txt", "r") as f:
    print("Содержимое файла:")
    print(f.read())