from abc import abstractmethod, ABC

class Animal(ABC):
    def __init__(self, name, energy):
        self.name = name
        self.__energy = energy

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if self.__energy < 0:
            raise ValueError("Энергия не может быть отрицательной!")

        self.__energy = value

    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def make_sound(self):
        print("Р-р-р!")
        self.energy -= 5

class Snake(Animal):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def make_sound(self):
        print("Ш-ш-ш!")
        self.energy -= 8

class Bird(Animal):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def make_sound(self):
        print("Ку-ку-ку!")
        self.energy -= 10

class ZooKeeper:
    def feed(self, animal):
        animal.energy += 15