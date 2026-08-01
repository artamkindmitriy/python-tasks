class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.height = 0
        self.speed = 0

    def print_info(self):
        print(f"Высота: {self.height}, Скорость: {self.speed}")

class Butterfly(CanFly):
    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5

class Rocket(CanFly):
    def take_off(self):
        self.height = 500
        self.speed = 1000

    def land(self):
        self.height = 0
        self.speed = 0
        self.explode()

    def explode(self):
        print("Ракета взорвалась!")