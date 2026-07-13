## Тема: Типизация и области видимости

### Задача 1. Функция с контрактом

**Дано:** Напишите функцию `calculate_area`, которая принимает два аргумента: `width` (float) и `height` (float), и возвращает их произведение (float). Используйте аннотации типов для аргументов и возвращаемого значения. Запросите ввод данных у пользователя и выведите результат работы функции.

**Решение:**

```python
from typing import List

def calculate_area(width: float, height: float) -> float:
    return width * height

w = float(input("Введите ширину: "))
h = float(input("Введите высоту: "))

area = calculate_area(w, h)
print(f"Площадь: {area}")
```

### Задача 2. Глобальный логгер ошибок

**Дано:** Создайте глобальную переменную `error_count = 0`. Напишите функцию `register_error()`, которая увеличивает `error_count` на 1 при каждом вызове (используйте `global`). Вызовите функцию три раза и выведите текущее значение `error_count`.

**Решение:**

```python
error_count = 0

def register_error():
    global error_count
    error_count += 1

    return error_count

register_error()
register_error()
print(f"Значение функции: {register_error()}")
```