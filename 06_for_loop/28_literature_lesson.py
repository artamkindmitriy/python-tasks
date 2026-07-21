grade = 0

for i in range(6):
    question = input("Кто написал произведение Евгений Онегин? ")
    if question != "Пушкин":
        print("Неправильно! Два тебе!")
        grade += 1
        continue
    elif question == "Пушкин":
        print("Правильно!")
        continue

print("Кол-во двоечников:", grade)