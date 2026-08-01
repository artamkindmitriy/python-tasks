import random

class Unit:
    def __init__(self, name):
        self.__health = 100
        self.name = name

    def take_damage(self):
        self.__health -= 20

    @property
    def get_hp(self):
        return self.__health

class Voin1(Unit):
    def __init__(self, name):
        super().__init__(name)

class Voin2(Unit):
    def __init__(self, name):
        super().__init__(name)

voin1 = Voin1("Рыцарь")
voin2 = Voin2("Дракон")

while True:
    attacker = random.choice([voin1, voin2])

    if attacker == voin1:
        defender = voin2
    else:
        defender = voin1

    defender.take_damage()

    print(f"{attacker.name} атаковал {defender.name}. У противника осталось здоровья: {defender.get_hp}")

    if defender.get_hp <= 0:
        print(f"Победил {attacker.name}!")
        break