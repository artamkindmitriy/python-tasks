count_students = int(input("Сколько в классе учеников? "))

grade_3 = 0
grade_4 = 0
grade_5 = 0

for grade in range(1, count_students + 1):
    grades = int(input("Введите оценку ученика: "))

    if grades == 3:
        grade_3 += 1
    elif grades == 4:
        grade_4 += 1
    elif grades == 5:
        grade_5 += 1
    else:
        print("Введите корректную оценку")

if grade_3 > grade_4 and grade_3 > grade_5:
    print("Сегодня больше троечников!")
elif grade_4 > grade_5:
    print("Сегодня больше хорошистов!")
else:
    print("Сегодня больше отличников!")