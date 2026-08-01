class Student:
    def __init__(self, fullname, n_group, grade):
        self.fullname = fullname
        self.n_group = n_group
        self.grade = grade

    def get_average_grade(self):
        return sum(self.grade) / len(self.grade)

    def __str__(self):
        return f"{self.fullname} | Группа {self.n_group} | Средний балл: {self.get_average_grade()}"

students = [
    Student("Иванов Иван", "П-11", [4, 5, 4, 3, 5]),
    Student("Петров Петр", "П-12", [5, 5, 5, 5, 5]),
    Student("Сидорова Анна", "П-11", [3, 4, 3, 4, 3]),
]

sorted_students = sorted(students, key=lambda student: student.get_average_grade())
for student in sorted_students:
    print(student)