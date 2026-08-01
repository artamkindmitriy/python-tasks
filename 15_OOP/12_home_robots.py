class Robot:
    def __init__(self, n_model):
        self.n_model = n_model

    def operate(self):
        print(f"Робот модель: {self.n_model}")

class RobotCleaner(Robot):
    def __init__(self, n_model, bag=0):
        super().__init__(n_model)
        self.bag = bag

    def operate(self):
        super().operate()
        print(f"Пылесошу пол. Текущая заполняемость мешка: {self.bag}")

class RobotSecurity(Robot):
    def __init__(self, n_model):
        super().__init__(n_model)

    def operate(self):
        super().operate()
        print("Патрулирую дом с помощью сигнализации.")

class RobotSwimming(RobotSecurity):
    def __init__(self, n_model, depth):
        super().__init__(n_model)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f"Охрана ведётся под водой. Глубина: {self.depth} м.")

cleaner = RobotCleaner("CleanBot-3000", 15)
cleaner.operate()

print("-" * 30)

swimming_robot = RobotSwimming("AquaGuard-X", 5)
swimming_robot.operate()