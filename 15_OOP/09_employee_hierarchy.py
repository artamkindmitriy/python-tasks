class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} работает")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def code(self):
        print(f"{self.name} пишет код на {self.language}")

dev = Developer("Иван", 150000, "Python")
dev.work()  # Выведет: Иван работает
dev.code()  # Выведет: Иван пишет код на Python