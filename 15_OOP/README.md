## **Тема: ООП**

### **Задача 1. Машина (Классы и объекты)**

**Дано:** Напишите класс Toyota, состоящий из четырёх статических атрибутов:

- цвет машины (например, красный),
- цена (один миллион),
- максимальная скорость (200),
- текущая скорость (ноль).

Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.

**Решение:**

```python
import random

class Toyota:
    color = "red"
    price = 1_000_000
    max_speed = 200
    current_speed = 0

car_1 = Toyota()
car_1.current_speed = random.randint(0, 200)

car_2 = Toyota()
car_2.current_speed = random.randint(0, 200)

car_3 = Toyota()
car_3.current_speed = random.randint(0, 200)

print(f"Скорость первой машины: {car_1.current_speed} км/ч")
print(f"Скорость второй машины: {car_2.current_speed} км/ч")
print(f"Скорость третьей машины: {car_3.current_speed} км/ч")
```

### **Задача 2. Однотипные объекты**

**Дано:** В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть четыре характеристики: название производителя, матрица, разрешение и частота обновления экрана. Все четыре монитора отличаются только частотой.

У наушников три характеристики: название производителя, чувствительность и наличие микрофона. Отличие только в наличии микрофона.

Для внесения в базу программист начал писать такой код:

```python
monitor_name_1 = 'Samsung'

monitor_matrix_1 = 'VA'

monitor_res_1 = 'WQHD'

monitor_freq_1 = 60

monitor_name_2 = 'Samsung'

monitor_matrix_2 = 'VA'

monitor_res_2 = 'WQHD'

monitor_freq_2 = 144

monitor_name_3 = 'Samsung'

monitor_matrix_3 = 'VA'

monitor_res_3 = 'WQHD'

monitor_freq_3 = 70

monitor_name_4 = 'Samsung'

monitor_matrix_4 = 'VA'

monitor_res_4 = 'WQHD'

monitor_freq_4 = 60

headphones_name_1 = 'Sony'

headphones_sensitivity_1 = 108

headphones_micro_1 = False

headphones_name_2 = 'Sony'

headphones_sensitivity_2 = 108

headphones_micro_2 = True

headphones_name_3 = 'Sony'

headphones_sensitivity_3 = 108

headphones_micro_3 = True
```

Поправьте программиста: перепишите код, используя классы и экземпляры классов.

**Решение:**

```python
class Monitor:
    def __init__(self, freq):
        self.name = "Samsung"
        self.matrix = "VA"
        self.freq = freq

    def __str__(self):
        return f"Монитор {self.name} (Матрица: {self.matrix}, Частота: {self.freq} Гц)"

class Headphones:
    def __init__(self, has_micro):
        self.name = "Sony"
        self.sensitivity = 108
        self.has_micro = has_micro

    def __str__(self):
        return f"Наушники {self.name} (Чувствительность: {self.sensitivity}, Есть микрофон: {self.has_micro})"

monitor_1 = Monitor(60)
monitor_2 = Monitor(144)
monitor_3 = Monitor(70)
monitor_4 = Monitor(60)

headphones_1 = Headphones(False)
headphones_2 = Headphones(True)
headphones_3 = Headphones(True)

print(monitor_1)
print(monitor_2)
print(monitor_3)
print(monitor_4)

print()

print(headphones_1)
print(headphones_2)
print(headphones_3)
```

### **Задача 3. Машина 2**

**Дано:** Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:

- цвет машины (например, красный),
- цена (один миллион),
- максимальная скорость (200),
- текущая скорость (ноль).

Добавьте два метода класса:

1. Отображение информации об объекте класса.
2. Метод, который позволяет устанавливать текущую скорость машины.

Проверьте работу этих методов.

**Решение:**

```python
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
```

### **Задача 4. Координаты точки**

**Дано:** Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.

Реализуйте класс, который будет представлять эту точку, и напишите метод, который предоставляет информацию о ней. Также внутри класса пропишите счётчик, который будет отвечать за количество созданных точек.

Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе **init**.

**Решение:**

```python
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
```

### Задача 5. Умная дверь (Инкапсуляция)

**Дано:** Создай класс `SmartDoor`. У двери есть состояние: заперта она или нет (`is_locked`), и уровень заряда батареи (`battery_level`).

- Сделай оба атрибута приватными.
- Реализуй методы `lock()` и `unlock()`. Дверь можно разблокировать, только если заряд батареи > 0.
- При попытке разблокировать дверь, если заряд 0, метод должен выводить: «Батарея разряжена!».
- Реализуй метод `charge()`, который восстанавливает заряд до 100%.

**Решение:**

```python
class SmartDoor:
    def __init__(self, charge):
        self.__is_locked = True
        self.__battery_level = charge

    def lock(self):
        self.__is_locked = True
        print("Дверь заперта.")

    def unlock(self):
        if self.__battery_level > 0:
            print("Дверь открыта")
            self.__is_locked = False
        else:
            print("Батарея разряжена!")

    def charge(self):
        print("Заряжаю батарею...")
        self.__battery_level = 100
        print("Батарея заряжена")

door = SmartDoor(0)

door.unlock()
door.charge()
door.unlock()
door.lock()
```

### Задача 6. Защищенный банкомат

**Дано:** Реализуйте класс `BankAccount`, который имитирует работу банковского счета.

1. У класса должен быть приватный атрибут `__balance`, который хранит текущую сумму денег на счете (начальное значение — 0).
2. Реализуйте метод `deposit(amount)`, который принимает сумму и добавляет её к балансу, только если переданная сумма положительная. Если сумма отрицательная или равна нулю, метод должен выводить сообщение об ошибке.
3. Реализуйте метод `withdraw(amount)`, который списывает сумму со счета, только если на балансе достаточно средств и сумма списания положительная. Если средств недостаточно или сумма некорректна, метод должен выводить соответствующее сообщение.
4. Реализуйте метод `get_balance()`, который возвращает текущее значение баланса.
5. Обеспечьте инкапсуляцию: к атрибуту `__balance` не должно быть прямого доступа извне (например, через `account.__balance` должно возникать исключение).

*Пример:*

```python
account = BankAccount()
account.deposit(1000)
print(account.get_balance())  # Выведет: 1000

account.withdraw(500)
print(account.get_balance())  # Выведет: 500

account.withdraw(2000)        # Выведет сообщение о нехватке средств
```

**Решение:**

```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной!")

        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Недостаточно средств.")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной!")

        self.__balance -= amount

    def get_balance(self):
        return f"Текущее состояние баланса: {self.__balance}"

account = BankAccount()
account.deposit(1000)
print(account.get_balance())  # Выведет: 1000

account.withdraw(500)
print(account.get_balance())  # Выведет: 500

account.withdraw(2000)  # Выведет сообщение о нехватке средств
```

### Задача 7. Кофемашина

**Дано:** Разработать класс для управления кофейным аппаратом. Объект должен хранить уровень воды (мл) и количество кофейных зерен (граммы) в приватных атрибутах. При создании объекта параметры задаются пользователем (по умолчанию 0). 

- Реализовать методы для пополнения ресурсов (`add_water`, `add_beans`). Установить верхний предел хранения: 1000 мл для воды и 500 г для зерен. При попытке превысить лимит или передаче отрицательного значения — возбуждать `ValueError`.
- Реализовать метод `make_coffee()`. Один цикл приготовления расходует 200 мл воды и 20 г зерен. Метод должен проверять достаточность ресурсов перед приготовлением и изменять состояние объекта.
- Реализовать метод `get_status()`, возвращающий текущий остаток ресурсов в формате строки.

**Решение:**

```python
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
```

### Задача 8. Безопасный пароль

**Дано:** Разработать класс для безопасного управления паролем пользователя. Объект хранит пароль в приватном атрибуте. При создании пароль должен проходить проверку: длина строки не менее 8 символов. В противном случае — `ValueError`.

- Реализовать метод `change_password(old_password, new_password)`. Смена пароля возможна только при условии, что `old_password` верный, а `new_password` соответствует требованиям сложности (длина >= 8).
- Реализовать метод `get_password_masked()`. Метод должен возвращать строку, скрывающую реальный пароль (например, маска фиксированной длины `*******` ). Прямой доступ к паролю извне должен быть исключен.

**Решение:**

```python
class ManagePassword:
    def __init__(self, password):
        if len(password) < 8:
            raise ValueError("Минимальная длина пароля - 8 символов.")

        self.__current_password = password

    def change_password(self, old_password, new_password):
        if old_password != self.__current_password:
            raise ValueError("Вы ввели неверный пароль.")

        if len(new_password) >= 8:
            print("Смена пароля успешна!")
            self.__current_password = new_password
        else:
            raise ValueError("Новый пароль не может быть короче 8 символов.")

    def get_password_masked(self):
        return "*" * len(self.__current_password)

```

### Задача 9. Иерархия сотрудников (Наследование)

**Дано:** Вам нужно спроектировать систему классов для учета сотрудников компании, используя принципы наследования.

1. Создайте базовый класс `Employee`. У каждого сотрудника должны быть атрибуты: `name` (имя) и `salary` (зарплата).
2. В классе `Employee` реализуйте метод `work()`, который выводит на экран сообщение: «[Имя] работает».
3. Создайте дочерний класс `Developer`, который наследует все атрибуты и методы от `Employee`.
4. В классе `Developer` добавьте новый атрибут `language` (язык программирования, на котором пишет разработчик) и новый метод `code()`, который выводит сообщение: «[Имя] пишет код на [язык]».
5. Создайте экземпляр класса `Developer` и проверьте, работают ли методы `work()` и `code()`.

*Пример:*

```python
dev = Developer("Иван", 150000, "Python")
dev.work()  # Выведет: Иван работает
dev.code()  # Выведет: Иван пишет код на Python
```

**Решение:**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} работает")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def code(self):
        print(f"{self.name} пишет код на {self.language}")

dev = Developer("Иван", 150000, "Python")
dev.work()  # Выведет: Иван работает
dev.code()  # Выведет: Иван пишет код на Python
```

### **Задача 10. Автомобили**

**Дано:** Даны два класса автомобилей: грузовой и легковой. У каждого из этих автомобилей есть своя модель, и каждый может сделать два действия: сообщить свою модель и поехать.

Грузовой автомобиль имеет такой атрибут, как заполненность багажника, изначально он равен нулю. У него есть ещё два действия: загрузить и разгрузить багажник.

У легкового автомобиля нет багажника, но есть навигационная система, которая передаётся вместе с моделью. Также вместо загрузки и разгрузки у него есть другое действие — включить навигацию.

Реализуйте классы грузового и легкового автомобилей. Для этого выделите общие атрибуты и методы в отдельный класс «Автомобиль» и используйте наследование. Не забудьте о функции super в дочерних классах.

*Пример:*

```python
car = Car("Toyota", "GPS")
car.get_info()  # У меня Toyota модель!
car.go()  # Модель Toyota поехала!
car.turn_on_nav()  # Навигация GPS включена!

truck = Gruzovik("Kamaz")
truck.get_info()  # У меня Kamaz модель!
truck.go()  # Модель Kamaz поехала!
truck.load()  # Багажник загружен!
truck.unload()  # Багажник разгружен!
```

**Решение:**

```python
class Auto:
    def __init__(self, model):
        self.model = model

    def get_info(self):
        print(f"У меня {self.model} модель!")

    def go(self):
        print(f"Модель {self.model} поехала!")

class Car(Auto):
    def __init__(self, model, nav):
        super().__init__(model)
        self.nav = nav

    def turn_on_nav(self):
        print(f"Навигация {self.nav} включена!")

class Gruzovik(Auto):
    def __init__(self, model, fullness=0):
        super().__init__(model)
        self.fullness = fullness

    def load(self):
        print("Багажник загружен!\n"
              f"Занято: {self.fullness}")

    def unload(self):
        print("Багажник разгружен!\n"
              f"Занято: {self.fullness}")
        self.fullness = 0

car = Car("Toyota", "GPS")
car.get_info()  # У меня Toyota модель!
car.go()  # Модель Toyota поехала!
car.turn_on_nav()  # Навигация GPS включена!

truck = Gruzovik("Kamaz")
truck.get_info()  # У меня Kamaz модель!
truck.go()  # Модель Kamaz поехала!
truck.load()  # Багажник загружен!
truck.unload()  # Багажник разгружен!
```

### Задача 11. Магазин электроники

**Дано:** Создай базовый класс `Device` (бренд, цена).

- Создай дочерние классы `Smartphone` и `Laptop`.
- В `Smartphone` добавь атрибут `operating_system` (Android/iOS) и метод `call()`.
- В `Laptop` добавь атрибут `ram_size` и метод `run_program()`.
- Используй `super().__init__` для инициализации общих атрибутов (бренд, цена).
- Проверь иерархию с помощью `isinstance()` и `issubclass()`.

**Решение:**

```python
class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class Smartphone(Device):
    def __init__(self, brand, price, operating_system):
        super().__init__(brand, price)
        self.operating_system = operating_system

    def call(self):
        pass

class Laptop(Device):
    def __init__(self, brand, price, ram_size):
        super().__init__(brand, price)
        self.ram_size = ram_size

    def run_program(self):
        pass

laptop = Laptop("Apple", 100000, 1000)
smartphone = Smartphone("Samsung", 10000, "iOS")

print(isinstance(laptop, Laptop))
print(isinstance(smartphone, Smartphone))
print()

print(issubclass(Laptop, Device))
print(issubclass(Smartphone, Device))
```

### **Задача 12. Домашние роботы**

**Дано:** На выставку робототехники привезли несколько интересных моделей роботов, которые похожи между собой, но немного различаются функциональностью. У каждого робота есть номер модели и действие operate, которое описывает выполняемые им функции.

Особенности роботов:

- У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает, что он пылесосит пол, и выводит текущую заполняемость мешка.
- У робота-охранника есть сигнализация, и при команде operate он выводит сообщение о патрулировании дома с её помощью.
- Ещё есть робот для бассейнов, который также является охранником. У этого робота есть значение глубины, и при команде operate он делает то же, что и робот-охранник, плюс сообщает, что охрана ведётся под водой.

Напишите программу, которая реализует все необходимые классы роботов.

**Решение:**

```python
class Robot:
    def __init__(self, n_model):
        self.n_model = n_model

    def operate(self):
        print(f"Робот модель: {self.n_model}")

class RobotCleaner(Robot):
    def __init__(self, n_model, bag=0):
        super().__init__(n_model)
        self.bag = bag

    def operate(self):
        super().operate()
        print(f"Пылесошу пол. Текущая заполняемость мешка: {self.bag}")

class RobotSecurity(Robot):
    def __init__(self, n_model):
        super().__init__(n_model)

    def operate(self):
        super().operate()
        print("Патрулирую дом с помощью сигнализации.")

class RobotSwimming(RobotSecurity):
    def __init__(self, n_model, depth):
        super().__init__(n_model)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f"Охрана ведётся под водой. Глубина: {self.depth} м.")

cleaner = RobotCleaner("CleanBot-3000", 15)
cleaner.operate()

print("-" * 30)

swimming_robot = RobotSwimming("AquaGuard-X", 5)
swimming_robot.operate()
```

### **Задача 13. Юниты (Полиморфизм)**

**Дано:** Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие «получить урон» (базовый класс получает 0 урона).

Также есть два дочерних класса:

- Солдат: получает урон, равный переданному значению.
- Обычный гражданин: получает урон, равный двукратному переданному значению.

Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).

**Решение:**

```python
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
```

### Задача 14. Музыкальные инструменты

**Дано:** Реализуйте систему классов, демонстрирующую принцип полиморфизма при работе с музыкальными инструментами.

1. Создайте три отдельных класса: `Guitar`, `Piano` и `Flute`.
2. В каждом из этих классов реализуйте метод `play()`.
    - Метод `play()` в классе `Guitar` должен возвращать строку: "Дзынь!".
    - Метод `play()` в классе `Piano` должен возвращать строку: "Бам!".
    - Метод `play()` в классе `Flute` должен возвращать строку: "Ту-ту!".
3. Создайте список, в который поместите по одному экземпляру каждого из этих классов.
4. Напишите цикл, который перебирает этот список и для каждого объекта вызывает метод `play()`, выводя результат на экран.

*Пример:*

```
Дзынь!
Бам!
Ту-ту!
```

**Решение:**

```python
class Guitar:
    def play(self):
        print("Дзынь!")

class Piano:
    def play(self):
        print("Бам!")

class Flute:
    def play(self):
        print("Ту-ту!")

guitar = Guitar()
piano = Piano()
flute = Flute()

music_tools = [guitar, piano, flute]

for tool in music_tools:
    tool.play()
```

### **Задача 15. Полёт**

**Дано:** Реализуйте класс «Может летать».

Атрибуты:

- Высота = 0.
- Скорость = 0.

Методы:

- Взлететь (в теле прописать pass).
- Лететь (в теле прописать pass).
- Приземлиться (установить высоту и скорость в значение 0).
- Вывести высоту и скорость на экран.

Затем реализуйте два дочерних класса:

«Бабочка», который может:

- Взлететь (высота = 1).
- Лететь (скорость = 0.5).

«Ракета», которая может:

- Взлететь (высота = 500, скорость = 1000).
- Приземлиться (высота = 0, взрыв).
- Взорваться (тут уже что угодно).

**Решение:**

```python
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
```

### Задача 16. Платежная система

**Дано:** Создай базовый класс `PaymentSystem`.
В нем должен быть метод `process_payment(amount)`, тело которого содержит `pass`. Создай два дочерних класса: `CreditCard` и `PayPal`, которые наследуются от `PaymentSystem`. Реализуй метод `process_payment(amount)` в обоих классах:

- **CreditCard**: выводит на экран текст `"Оплата [amount] руб. картой через терминал"`, подставляя переданную сумму.
- **PayPal**: выводит на экран текст `"Оплата [amount] руб. через PayPal-аккаунт"`, подставляя переданную сумму.

**Решение:**

```python
class PaymentSystem:
    def process_payment(self, amount):
        pass

class CreditCard(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата {amount} руб. картой через терминал")

class PayPal(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата {amount} руб. через PayPal-аккаунт")
```

### Задача 17. Фигуры (Абстракция)

**Дано:** Реализуйте систему классов для вычисления площади геометрических фигур, используя абстрактные классы.

1. Создайте абстрактный базовый класс `Shape`, который будет служить шаблоном для всех фигур.
2. В классе `Shape` определите абстрактный метод `area()`, который не имеет реализации (в теле метода напишите `pass`), но должен быть обязателен для реализации в дочерних классах.
3. Создайте дочерний класс `Rectangle` (прямоугольник):
    ◦ Конструктор должен принимать ширину и высоту.
    ◦ Метод `area()` должен возвращать площадь прямоугольника (ширина × высота).
4. Создайте дочерний класс `Circle` (круг):
    ◦ Конструктор должен принимать радиус.
    ◦ Метод `area()` должен возвращать площадь круга. Для значения pi воспользуйтесь библиотекой `math`.
5. Проверьте работу программы: создайте экземпляры `Rectangle` и `Circle`, вызовите у них метод `area()` и выведите результаты на экран.

**Решение:**

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2)

rectangle = Rectangle(10, 20)
circle = Circle(10)

print(rectangle.area())
print(circle.area())
```

### **Задача 18. Координаты точки. Геттер + Сеттер**

**Дано:** В одной из практик предыдущего модуля была задача на реализацию класса «Точка». Модернизируйте класс по следующему условию: объект «Точка» на плоскости имеет координаты x и y; при создании новой точки могут передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.

Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:

1. Предоставление информации о точке (используйте магический метод str).
2. Геттер и сеттер для x.
3. Геттер и сеттер для y.

Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.

**Решение:**

```python
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
```

### Задача 19. Безопасный банковский вклад

**Дано:** Создай класс `BankAccount`.

- Есть приватный атрибут `__balance`.
- Реализуй геттер для чтения баланса.
- Реализуй сеттер для изменения баланса, но с жесткими правилами:
    - Ты не можешь установить баланс меньше 0.
    - Ты не можешь изменить баланс, если новая сумма отличается от старой более чем на 1 000 000 (лимит на одну операцию). Если попытка нарушает лимит — выводи ошибку.

**Решение:**

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Ты не можешь установить баланс меньше нуля")
        elif abs(value - self._balance) > 1_000_000:
            raise ValueError("Старая сумма не может отличаться от новой на 1_000_000 рублей")

        self._balance = value
```

### **Задача 20. Драка (Комбинированные задачи)**

**Дано:** Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.

Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье в 100 очков. Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

**Решение:**

```python
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
```

### **Задача 21. Студенты**

**Дано:** Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов). Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя) и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.

**Решение:**

```python
class Student:
    def __init__(self, fullname, n_group, grade):
        self.fullname = fullname
        self.n_group = n_group
        self.grade = grade

    def get_average_grade(self):
        return sum(self.grade) / len(self.grade)

    def __str__(self):
        return f"{self.fullname} | Группа {self.n_group} | Средний балл: {self.get_average_grade()}"

students = [
    Student("Иванов Иван", "П-11", [4, 5, 4, 3, 5]),
    Student("Петров Петр", "П-12", [5, 5, 5, 5, 5]),
    Student("Сидорова Анна", "П-11", [3, 4, 3, 4, 3]),
]

sorted_students = sorted(students, key=lambda student: student.get_average_grade())
for student in sorted_students:
    print(student)
```

### **Задача 22. Отцы, матери и дети**

**Дано:** Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:

- имя,
- возраст,
- список детей.

И он может:

- сообщить информацию о себе,
- успокоить ребёнка,
- покормить ребёнка.

У ребёнка есть:

- имя,
- возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
- состояние спокойствия,
- состояние голода.

Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее.

**Решение:**

```python
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
```

### Задача 23. Зоопарк

**Дано:** Создай абстрактный класс `Animal` (имя, метод `make_sound`).

- Создай классы `Lion`, `Snake`, `Bird` (наследуются от `Animal`).
- Сделай атрибут `__energy` у всех животных.
- Создай класс `ZooKeeper` (смотритель). Он должен уметь кормить животных (`feed(animal)`), при этом метод `feed` должен увеличивать `__energy` животного (используй сеттер для изменения энергии).
- При вызове `make_sound` энергия животного должна немного уменьшаться.

**Решение:**

```python
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
```

---