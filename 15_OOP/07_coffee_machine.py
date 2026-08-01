class CoffeeMachine:
    MAX_WATER = 1000
    MAX_BEANS = 500

    def __init__(self, water=0, grains=0):
        if water < 0 or grains < 0:
            raise ValueError("Начальные ресурсы не могут быть отрицательными.")
        if water > self.MAX_WATER or grains > self.MAX_BEANS:
            raise ValueError("Начальные ресурсы превышают лимиты емкости.")

        self.__water_level = water
        self.__coffee_beans = grains

    def add_water(self, amount_water):
        if amount_water <= 0:
            raise ValueError("Можно добавить только положительное кол-во воды.")

        if self.__water_level + amount_water > self.MAX_WATER:
            raise ValueError(f"Превышен лимит воды! Максимум {self.MAX_WATER} мл.")

        self.__water_level += amount_water

    def add_beans(self, amount_beans):
        if amount_beans <= 0:
            raise ValueError("Можно добавлять только положительное кол-во зерна.")

        if amount_beans + self.__coffee_beans > self.MAX_BEANS:
            raise ValueError(f"Превышен лимит зерна! Максимум {self.MAX_BEANS} г.")

        self.__coffee_beans += amount_beans

    def make_coffee(self):
        if self.__coffee_beans >= 20 and self.__water_level >= 200:
            print("Делаю кофе...")
            print("Готово, осторожно, горячо!")

            self.__coffee_beans -= 20
            self.__water_level -= 200
        else:
            raise ValueError("Недостаточно ресурсов для приготовления кофе.")

    def get_status(self):
        return (f"Текущее состояние ресурсов:\n"
                f"Зерна: {self.__coffee_beans} г\n"
                f"Вода: {self.__water_level} мл")