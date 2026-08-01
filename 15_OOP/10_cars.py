class Auto:
    def __init__(self, model):
        self.model = model

    def get_info(self):
        print(f"У меня {self.model} модель!")

    def go(self):
        print(f"Модель {self.model} поехала!")

class Car(Auto):
    def __init__(self, model, nav):
        super().__init__(model)
        self.nav = nav

    def turn_on_nav(self):
        print(f"Навигация {self.nav} включена!")

class Gruzovik(Auto):
    def __init__(self, model, fullness=0):
        super().__init__(model)
        self.fullness = fullness

    def load(self):
        print("Багажник загружен!\n"
              f"Занято: {self.fullness}")

    def unload(self):
        print("Багажник разгружен!\n"
              f"Занято: {self.fullness}")
        self.fullness = 0

car = Car("Toyota", "GPS")
car.get_info()  # У меня Toyota модель!
car.go()  # Модель Toyota поехала!
car.turn_on_nav()  # Навигация GPS включена!

truck = Gruzovik("Kamaz")
truck.get_info()  # У меня Kamaz модель!
truck.go()  # Модель Kamaz поехала!
truck.load()  # Багажник загружен!
truck.unload()  # Багажник разгружен!