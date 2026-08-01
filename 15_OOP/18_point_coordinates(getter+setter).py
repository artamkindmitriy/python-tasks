class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Точка x: {self.x}, Точка y: {self.y}"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Координаты должны быть числом!")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Координаты должны быть числом!")
        self._y = value