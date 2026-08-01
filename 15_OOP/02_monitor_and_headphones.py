class Monitor:
    def __init__(self, freq):
        self.name = "Samsung"
        self.matrix = "VA"
        self.freq = freq

    def __str__(self):
        return f"Монитор {self.name} (Матрица: {self.matrix}, Частота: {self.freq} Гц)"

class Headphones:
    def __init__(self, has_micro):
        self.name = "Sony"
        self.sensitivity = 108
        self.has_micro = has_micro

    def __str__(self):
        return f"Наушники {self.name} (Чувствительность: {self.sensitivity}, Есть микрофон: {self.has_micro})"

monitor_1 = Monitor(60)
monitor_2 = Monitor(144)
monitor_3 = Monitor(70)
monitor_4 = Monitor(60)

headphones_1 = Headphones(False)
headphones_2 = Headphones(True)
headphones_3 = Headphones(True)

print(monitor_1)
print(monitor_2)
print(monitor_3)
print(monitor_4)

print()

print(headphones_1)
print(headphones_2)
print(headphones_3)