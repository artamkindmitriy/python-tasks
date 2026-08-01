class Parent:
    def __init__(self, name, age, children=None):
        self.name = name
        self._age = age
        self.children = []

        if children:
            for child in children:
                self.add_child(child)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        for child in self.children:
            if value - child.age < 16:
                raise ValueError(f"Нельзя установить такой возраст родителя: разница с ребенком {child.name} меньше 16 лет!")
        self._age = value

    def add_child(self, child):
        """Метод для добавления ребенка с проверкой возраста"""
        if self._age - child.age < 16:
            raise ValueError(f"Родитель {self.name} слишком молод для ребенка {child.name}!")

        child.parent = self
        self.children.append(child)

    def get_info(self):
        print(f"Меня зовут: {self.name} | Мне {self._age} лет | Детей: {len(self.children)}")

    def calm_child(self, child):
        child.is_calm = True
        print(f"Родитель {self.name} успокоил ребенка {child.name}.")

    def feed_child(self, child):
        child.is_hungry = False
        print(f"Родитель {self.name} покормил ребенка {child.name}.")

class Child:
    def __init__(self, name, age, is_calm=False, is_hungry=True):
        self.name = name
        self._age = age
        self.feel_calm = is_calm
        self.feel_feed = is_hungry
        self.parent = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст ребенка не может быть отрицательным!")

        if self.parent and (self.parent.age - value < 16):
            raise ValueError(f"Нельзя установить такой возраст: разница с родителем {self.parent.name} меньше 16 лет!")

        self._age = value