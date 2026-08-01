class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def __str__(self):
        return (f"Информация о точке: x: {self.x}, y: {self.y}\n"
                f"Количество созданных точек: {self.count}")


while True:
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))

    point = Point(x, y)
    print(point)