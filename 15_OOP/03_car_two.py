class Toyota:
    def __init__(self, current_speed):
        self.color = "red"
        self.price = 1_000_000
        self.max_speed = 200

        if current_speed < 0:
            print("Ошибка: Скорость не может быть отрицательной! Устанавливаю 0")
            self.current_speed = 0
        else:
            self.current_speed = current_speed

    def __str__(self):
        return (f"Цвет: {self.color}, Цена: {self.price}, "
                f"Макс. скорость: {self.max_speed}, "
                f"Текущая скорость: {self.current_speed}")

set_speed_1 = int(input("Введите скорость для первой машины: "))
set_speed_2 = int(input("Введите скорость для второй машины: "))
set_speed_3 = int(input("Введите скорость для третьей машины: "))

car_1 = Toyota(set_speed_1)
car_2 = Toyota(set_speed_2)
car_3 = Toyota(set_speed_3)

print()

print(f"Первая машина: {car_1}")

print()
print(f"Вторая машина: {car_2}")

print()
print(f"Третья машина: {car_3}")