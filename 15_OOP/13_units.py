class Unit:
    def __init__(self, health):
        self._health = health

    def get_damage(self, damage):
        return 0

class Soldier(Unit):
    def __init__(self, health):
        super().__init__(health)

    def get_damage(self, damage):
        super().get_damage(damage)
        self._health -= damage
        return damage

class CityZen(Unit):
    def __init__(self, health):
        super().__init__(health)

    def get_damage(self, damage):
        super().get_damage(damage)
        self._health -= damage
        return damage * 2