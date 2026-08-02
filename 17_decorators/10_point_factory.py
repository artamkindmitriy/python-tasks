class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, coordinate_string):
        x, y = coordinate_string.split(";")

        return cls(int(x), int(y))

test = Point.from_string("10;20")

print(f"Координата х: {test.x}")
print(f"Координата y: {test.y}")