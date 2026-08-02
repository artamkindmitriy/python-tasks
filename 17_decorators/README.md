## **Тема: Декораторы**

### **Задача 1. Удвоитель**

**Дано:** Напиши декоратор `double_result`, который принимает функцию, возвращающую число, и умножает это число на 2.

**Решение:**

```python
from functools import wraps

def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value * 2
    return wrapper

@double_result
def test():
    return 2

print(test())
```

### **Задача 2. Повторитель**

**Дано:** Напиши декоратор `repeat_twice`, который вызывает декорируемую функцию дважды подряд.

*Пример:*

```python
@repeat_twice
def say_hi():
    print("Привет!")

# Вызов say_hi() должен напечатать "Привет!" два раза.
```

**Решение:**

```python
from functools import wraps

def repeat_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@repeat_twice
def say_hi():
    print("Привет!")

say_hi()

# Вызов say_hi() должен напечатать "Привет!" два раза.
```

### **Задача 3. Логгер-невидимка**

**Дано:** Напиши декоратор `debug_log`, который выводит в консоль фразу: *"Вызов функции [имя_функции]"* перед её выполнением. Обязательно используй `wraps`.

**Решение:**

```python
from functools import wraps

def debug_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@debug_log
def test(a, b):
    return a + b

result = test(3, 5)
print(f"Результат: {result}")
print(f"Имя функции: {test.__name__}")
print(f"Докстринг: {test.__doc__}")
```

### **Задача 4. Проверка прав**

**Дано:** Создай декоратор `require_auth`.

- Если переменная `is_authenticated = True`, он должен вызывать функцию.
- Если `False`, выводить: *"Доступ запрещен"*.
    
    Примени его к функции `get_secret_data()`. Убедись, что `get_secret_data.__name__` возвращает правильное имя, а не имя внутренней функции декоратора.
    

**Решение:**

```python
from functools import wraps

is_authenticated = True

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            return "Доступ запрещён"
    return wrapper

@require_auth
def get_secret_data():
    return "Секретный документ: 12345"

print(get_secret_data())
```

### **Задача 5. Умножитель результата**

**Дано:** Напиши декоратор `multiply(factor)`, который принимает число `factor` и умножает на него результат возвращаемого значения функции.

*Пример:* Если функция возвращает 10, а декоратор вызван как `@multiply(3)`, итоговый результат должен быть 30.

**Решение:**

```python
from functools import wraps

def multiply(factor):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return factor * func(*args, **kwargs)
        return wrapper
    return decorator

@multiply(3)
def check():
    return 10

print(check())
```

### **Задача 6. Доступ по роли**

**Дано:** Напиши декоратор `check_access(role)`, который проверяет строку, переданную в аргумент.

- Если `role == "admin"`, функция выполняется и печатает "Доступ разрешен".
- Если любая другая строка — функция не вызывается, а печатается "Ошибка: нет прав".

**Решение:**

```python
from functools import wraps

def check_access(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role != "admin":
                raise PermissionError("Ошибка: нет прав")
            else:
                print("Доступ разрешен")
                return func(*args, **kwargs)
        return wrapper
    return decorator

@check_access("admin")
def test_check_is_admin():
    pass

test_check_is_admin()
```

### **Задача 7. Логирование создания**

**Дано:** Напиши декоратор `@debug_init`, который при создании любого объекта класса будет печатать фразу: `"Создан объект класса [ИмяКласса]"`.

**Решение:**

```python
def debug_init(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"Создан объект класса {cls.__name__}")
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@debug_init
class Unit:
    def __init__(self, name):
        self.name = name

u1 = Unit("Воин")
u2 = Unit("Лучник")
```

### **Задача 8. Запрет на изменения**

**Дано:** Напиши декоратор `@frozen`, который добавляет в класс метод `__setattr__` так, чтобы после создания объекта нельзя было добавлять новые атрибуты (только менять существующие).

**Решение:**

```python
def frozen(cls):
    def add_method(self, name, value):
        if hasattr(self, name):
            object.__setattr__(self, name, value)
        else:
            raise AttributeError(f"Нельзя добавлять новые атрибуты: {name}")
        
    cls.__setattr__ = add_method
    return cls
```

### **Задача 9. Таймер выполнения**

**Дано:** Напиши декоратор `@measure_time`. Он должен замерять время выполнения метода и печатать: `"Метод [название] выполнился за X сек"`.

**Решение:**

```python
import time

def measure_time(func):
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        print(f"Метод {func.__name__} выполнился за {end_time - start_time:.4f} сек")
        return result
    return wrapper

class Tester:
    @measure_time
    def test(self):
        time.sleep(1)
        return "Успех"

obj = Tester()
obj.test()
```

### **Задача 10. Фабрика точек**

**Дано:** Создай класс `Point`. Обычный конструктор принимает координаты `x` и `y`. Напиши `@classmethod from_string(cls, coordinate_string)`, который принимает строку вида `"10;20"`, разделяет её по точке с запятой и возвращает новый объект `Point` с целочисленными координатами.

**Решение:**

```python
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
```

### **Задача 11. Конвертер температуры**

**Дано:** Создай класс `TemperatureConverter`. Напиши статический метод `celsius_to_fahrenheit(celsius)`, который переводит градусы Цельсия в Фаренгейты по формуле: `celsius * 9/5 + 32`. Метод должен вызываться напрямую через класс, без создания экземпляра.

**Решение:**

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        result = celsius * 9/5 + 32
        return result
```

---