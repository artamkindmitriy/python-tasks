## **Тема: Словари**

### **Задача 1. Словарь квадратов чисел**

**Дано:** На вход программе поступает целое число num. Напишите программу создания словаря, который включает в себя ключи от 1 до num, а значениями соответствующего ключа будет значение ключа в квадрате.

*Пример:*

```
Введите целое число: 5

Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Решение:**

```python
num = int(input("Введите целое число: "))
dict_numbers = {i: i ** 2 for i in range(1, num + 1)}

print(f"Результат:{dict_numbers}")
```

### **Задача 2. Студент**

**Дано:** Пользователь вводит фамилию, имя студента, город проживания, вуз, в котором он учится, и все его оценки. Всё вводится в одну строку через пробел. Напишите программу, которая по этой информации составит словарь и выведет его на экран.

*Пример:*

```
Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): Илья Иванов Москва МГУ 5 4 4 4 5

Имя - Илья

Фамилия - Иванов

Город - Москва

Место учёбы - МГУ

Оценки - [5, 4, 4, 4, 5]
```

**Решение:**

```python
information = input("Введите информацию о студенте через пробел\n"
                    " (имя, фамилия, город, место учёбы, оценки): ")

dict_inf = {}

words = information.split()

dict_inf["Имя"] = words[0]
dict_inf["Фамилия"] = words[1]
dict_inf["Город"] = words[2]
dict_inf["Место учёбы"] = words[3]
dict_inf["Оценки"] = [int(x) for x in words[4:]]

print()

for key, value in dict_inf.items():
    print(f"{key} -{value}")
```

### **Задача 3. Контакты**

**Дано:** Энтузиаст Степан, купив новый телефон, решил написать для него свою собственную операционную систему. И, конечно же, первое, что он захотел в ней реализовать, — это телефонная книга.

Напишите программу, которая запрашивает у пользователя имя контакта и номер телефона, добавляет их в словарь и выводит на экран текущий словарь контактов. Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы). Обеспечьте контроль ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.

*Пример:*

```
Текущие контакты на телефоне:

<Пусто>

Введите имя: Иван

Введите номер телефона: 100200300

Текущие контакты на телефоне:

Иван  100200300

Введите имя: Лена

Введите номер телефона: 8005555522

Текущие контакты на телефоне:

Иван  100200300

Лена  8005555522

Введите имя: Иван

Ошибка: такое имя уже существует.
```

**Решение:**

```python
contacts = {}

while True:
    print("Текущие контакты на телефоне:")
    if not contacts:
        print("<Пусто>")
    else:
        for name, phone_number in contacts.items():
            print(f"{name}{phone_number}")

    name = input("Введите имя (или 'стоп' для выхода): ")
    if name in contacts:
        print("Ошибка: такое имя уже существует")
    elif name.lower() == "стоп":
        print("Выходим из программы")
        break
    else:
        number_phone = int(input("Введите номер телефона: "))
        contacts[name] = number_phone
```

### **Задача 4. Заказ фруктов**

**Дано:** В торговую компанию пришёл заказ:

```
order = {
	'apple': 2,
	'banana': 3,
	'pear': 1,
	'watermelon': 10,
	'chocolate': 5
}
```

Ключи — названия товаров, значения — необходимое количество килограммов.

При помощи метода get и установки значения по умолчанию проверьте, есть ли товар на складе, и получите его цену. Если товара нет, то по умолчанию получите 0. Подсчитайте итоговую выручку компании по имеющимся товарам.

```
incomes = {
	'apple': 5600.20,
	'orange': 3500.45,
	'banana': 5000.00,
	'bergamot': 3700.56,
	'durian': 5987.23,
	'grapefruit': 300.40,
	'peach': 10000.50,
	'pear': 1020.00,
	'persimmon': 310.00,
}
```

Ключи — названия товаров, значения — цена за один килограмм.

Напишите программу, которая суммирует стоимость (цена × количество) всех заказанных товаров, и выведите итоговую сумму в консоль.

Если искомого товара нет на складе, то по умолчанию получите 0. В этом поможет метод get и установка значения по умолчанию.

**Решение:**

```python
order = {
	'apple': 2,
	'banana': 3,
	'pear': 1,
	'watermelon': 10,
	'chocolate': 5
}

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

total = 0

for product, quantity in order.items():
    price = incomes.get(product, 0)
    cost = price * quantity
    total += cost
    print(f"{product}:{quantity} кг *{price} руб ={cost} руб")

print(f"\nИтоговая выручка:{total} руб")
```

### **Задача 5. Игроки**

**Дано:** Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, а также его текущий статус, в котором указано, отдыхает он, тренируется или путешествует:

```
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
```

Напишите программу, которая выводит на экран следующие данные в разных строках:

1. Все члены команды А, которые отдыхают.
2. Все члены команды B, которые тренируются.
3. Все члены команды C, которые путешествуют.

**Решение:**

```python
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team_a_rest = []
team_b_training = []
team_c_travel = []

for team in players_dict.values():
    if team["team"] == "A" and team["status"] == "Rest":
        team_a_rest.append(team["name"])
    elif team["team"] == "B" and team["status"] == "Training":
        team_b_training.append(team["name"])
    elif team["team"] == "C" and team["status"] == "Travel":
        team_c_travel.append(team["name"])

print(f"Результат группы А:{team_a_rest}")
print(f"Результат группы B:{team_b_training}")
print(f"Результат группы C:{team_c_travel}")
```

### **Задача 6. Склады**

**Дано:** У мебельного магазина есть два склада, на которых хранятся разные категории товаров по парам «название — количество»:

```
small_storage = {
	'гвозди': 5000,
	'шурупы': 3040,
	'саморезы': 2000
}
```

```
big_storage = {
	'доски': 1000,
	'балки': 150,
	'рейки': 600
}
```

Магазин решил сократить аренду и скинуть все товары в большой склад (big_storage). После этого нас попросили реализовать поиск по товарам.

Напишите программу, которая объединяет оба словаря в один (в big_storage), затем запрашивает у пользователя название товара и выводит на экран его количество. Если такого товара нет, то выводит об этом ошибку. Для получения значения используйте метод get.

**Решение:**

```python
small_storage = {
	'гвозди': 5000,
	'шурупы': 3040,
	'саморезы': 2000
}

big_storage = {
	'доски': 1000,
	'балки': 150,
	'рейки': 600
}

combined = small_storage | big_storage

name_tool = input("Введите название товара: ")
result = combined.get(name_tool.lower(), "Такого товара нету на складе")
print(result)
```

### **Задача 7. Кризис фруктов**

**Дано:** Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год сохранены в словаре в виде пар «название фрукта — доход»:

```
incomes = {
	'apple': 5600.20,
	'orange': 3500.45,
	'banana': 5000.00,
	'bergamot': 3700.56,
	'durian': 5987.23,
	'grapefruit': 300.40,
	'peach': 10000.50,
	'pear': 1020.00,
	'persimmon': 310.00,
}
```

В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода.

Напишите программу, которая находит общий доход, затем выводит фрукт с минимальным доходом и удаляет его из словаря. Выведите итоговый словарь на экран.

*Пример:*

```
Общий доход за год составил 35419.34 рублей

Самый маленький доход у grapefruit. Он составляет 300.4 рублей

Итоговый словарь: {'apple': 5600.2, 'orange': 3500.45, 'banana': 5000.0, 'bergamot': 3700.56, 'durian': 5987.23, 'peach': 10000.5, 'pear': 1020.0, 'persimmon': 310.0}
```

**Решение:**

```python
incomes = {
	'apple': 5600.20,
	'orange': 3500.45,
	'banana': 5000.00,
	'bergamot': 3700.56,
	'durian': 5987.23,
	'grapefruit': 300.40,
	'peach': 10000.50,
	'pear': 1020.00,
	'persimmon': 310.00,
}

total_income = sum(incomes.values())

min_val = min(incomes.values())
min_product = min(incomes, key=incomes.get)

print(f"Общий доход за год составил{total_income} рублей")
print(f"Самый маленький доход у{min_product}. Он составляет{min_val} рублей")

incomes.pop(min_product)

print(f"Итоговый словарь:{incomes}")
```

### **Задача 8. Гистограмма частоты**

**Дано:** Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных будет строиться гистограмма частоты букв.

Напишите программу, которая получает сам текст и считает, сколько раз в строке встречается каждый символ. На экран нужно вывести содержимое в виде таблицы, отсортированное по алфавиту, а также максимальное значение частоты.

*Пример:*

```
Введите текст: Здесь что-то написано

  : 2

- : 1

З : 1

а : 2

д : 1

е : 1

и : 1

н : 2

о : 3

п : 1

с : 2

т : 2

ч : 1

ь : 1

Максимальная частота: 3
```

**Решение:**

```python
from collections import Counter
text = input("Введите текст: ")
counter = Counter(text)
sorted_dict = dict(sorted(counter.items()))
max_count = max(sorted_dict.values())
for symbol, count in sorted_dict.items():
    print(f"{symbol} :{count}")

print(f"Максимальная частота:{max_count}")
```

### **Задача 9. Песни — 2**

**Дано:** Продолжим писать приложение для удобного прослушивания музыки, но теперь песни хранятся в виде словаря, а не в виде вложенных списков. Каждая песня состоит из названия и продолжительности с точностью до долей минут.

```python
violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
```

Напишите программу, которая запрашивает у пользователя количество песен из списка и их названия, а на экран выводит общее время их звучания.

*Пример:*

```
Сколько песен выбрать? 3

Название первой песни: Halo

Название второй песни: Enjoy the Silence

Название третьей песни: Clean

Общее время звучания песен: 14,93 минуты
```

**Решение:**

```python
violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}

choose_songs = int(input("Сколько песен выбрать? "))

total_minute = 0

for songs in range(1, choose_songs + 1):
    song = input(f"Название{songs}-й песни: ")

    minutes = violator_songs.get(song, 0)

    if minutes == 0:
        print("Такой песни нет, она не будет учтена")
    else:
        total_minute += minutes

print(f"Общее время звучания песен:{total_minute} минуты")
```

### **Задача 10. Криптовалюта**

**Дано:** При работе с API сайта биржи по криптовалюте вы получили такие данные в виде словаря:

```python
data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
```

Теперь необходимо обработать эти данные.

Напишите программу, которая выполняет следующий алгоритм действий:

1. Вывести списки ключей и значений словаря.
2. В ETH добавить ключ total_diff со значением 100.
3. Внутри fst_token_info значение ключа name поменять с fdf на doge.
4. Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
5. Внутри sec_token_info изменить название ключа price на total_price.

После выполнения алгоритма выводить результат (словарь) не нужно.

**Решение:**

```python
data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print("Ключи:", list(data.keys()))
print("Значения:", list(data.values()))

data["ETH"]["total_diff"] = 100

data["tokens"][0]["fst_token_info"]["name"] = "doge"

total_out_sum = sum(token.pop("total_out", 0) for token in data["tokens"])
data["ETH"]["totalOut"] = total_out_sum

token_info = data["tokens"][1]["sec_token_info"]
if "price" in token_info:
    token_info["total_price"] = token_info.pop("price")

print("\nОбновленные данные:")
import json
print(json.dumps(data, indent=2, ensure_ascii=False))
```

### **Задача 11. Товары**

**Дано:** В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает за коды товаров, второй — за списки количества разнообразных товаров на складе:

```
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
```

Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров. Цена указана за одну штуку.

Напишите программу, которая рассчитывает общую стоимость позиций для каждого товара на складе и выводит эту информацию на экран.

*Пример:*

```
Лампа — 27 штук, стоимость 1134 рубля.

Стол — 54 штуки, стоимость 27 860 рублей.

Диван — 3 штуки, стоимость 3550 рублей.

Стул — 105 штук, стоимость 10 311 рублей.
```

**Решение:**

```python
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for name_product, code in goods.items():
    total_quantity = 0
    total_cost = 0

    purchases = store[code]
    for item in purchases:
        total_quantity += item['quantity']
        total_cost += item['price'] * item['quantity']

    print(f"{name_product} —{total_quantity} штук, стоимость{total_cost} рублей.")
```

### **Задача 12. Гистограмма частоты — 2**

**Дано:** Вы уже писали программу для лингвистов, которая получала на вход текст и считала, сколько раз каждый символ встречается в строке. Теперь задание изменилось: максимальную частоту выводить не нужно, но необходимо написать функцию, которая будет инвертировать полученный словарь. То есть в качестве ключа будет частота, а в качестве значения — список символов с этой частотой.

По итогу нужно реализовать следующие подзадачи:

1. получить текст и создать из него оригинальный словарь частот;
2. создать новый словарь и заполнить его данными из оригинального словаря частот, используя количество повторов в качестве ключей, а буквы — в качестве значений, добавляя их в список для хранения.

*Пример:*

```
Введите текст: здесь что-то написано

Оригинальный словарь частот:

: 2

- : 1

З : 1

а : 2

д : 1

е : 1

и : 1

н : 2

о : 3

п : 1

с : 2

т : 2

ч : 1

ь : 1

Инвертированный словарь частот:

1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']

2 : ['с', ' ', 'т', 'н', 'а']

3 : ['о']
```

**Решение:**

```python
def main():
    text = input("Введите текст: ")

    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    inverted_dict = {}
    for char, count in freq_dict.items():
        if count not in inverted_dict:
            inverted_dict[count] = []
        inverted_dict[count].append(char)

    print("\nОригинальный словарь частот:")
    for char in sorted(freq_dict.keys()):
        print(f"{char} :{freq_dict[char]}")

    print("\nИнвертированный словарь частот:")
    for count in sorted(inverted_dict.keys()):
        sorted_chars = sorted(inverted_dict[count])
        print(f"{count} :{sorted_chars}")

if __name__ == "__main__":
    main()
```

### **Задача 13. Анализ посещаемости**

**Дано:** У тебя есть словарь, где ключи — имена пользователей, а значения — списки сайтов, которые они посещали.

```python
users_history = {
    'Алексей': ['google.com', 'yandex.ru', 'google.com'],
    'Марина': ['wikipedia.org', 'google.com', 'wikipedia.org', 'python.org'],
    'Иван': ['python.org', 'google.com']
}
```

Напиши программу, которая выводит уникальный список посещенных сайтов для каждого пользователя (удаляет дубликаты).

**Решение:**

```python
users_history = {
    'Алексей': ['google.com', 'yandex.ru', 'google.com'],
    'Марина': ['wikipedia.org', 'google.com', 'wikipedia.org', 'python.org'],
    'Иван': ['python.org', 'google.com']
}

for name, site in users_history.items():
    unique_sites = set(site)
    print(f"{name} -", *unique_sites)
```

### **Задача 14. Корзина интернет-магазина**

**Дано:** Дан словарь товаров с их ценами и словарь с тем, что купил пользователь

```python
prices = {'молоко': 80, 'хлеб': 40, 'сыр': 250, 'яйца': 120}
cart = {'молоко': 2, 'сыр': 1, 'кофе': 1}
```

Рассчитай общую стоимость покупки. Если товара нет в словаре `prices` (как кофе), программа должна выводить сообщение: «Товар [название] не найден, цена 0», и не прибавлять его к стоимости.

**Решение:**

```python
prices = {'молоко': 80, 'хлеб': 40, 'сыр': 250, 'яйца': 120}
cart = {'молоко': 2, 'сыр': 1, 'кофе': 1}

total_price = 0

for product, quantity in cart.items():
    price = prices.get(product)
    if price is not None:
        cost = price * quantity
        total_price += cost
        print(f"Товар{product}:{quantity} шт. *{price} руб. ={cost} руб.")
    else:
        print(f"Товар{product} не найден, цена 0")

print(f"\nИтоговая цена покупки:{total_price} рублей")
```

### **Задача 15. Переворот словаря**

**Дано:** Дан словарь, где ключ — город, а значение — название страны.

```python
cities = {'Москва': 'Россия', 'Берлин': 'Германия', 'Париж': 'Франция', 'Санкт-Петербург': 'Россия'}
```

Создай новый словарь, где ключами будут **страны**, а значениями — **списки городов** этой страны.

*Результат должен выглядеть так:* `{'Россия': ['Москва', 'Санкт-Петербург'], 'Германия': ['Берлин'], ...}`.

**Решение:**

```python
cities = {'Москва': 'Россия', 'Берлин': 'Германия', 'Париж': 'Франция', 'Санкт-Петербург': 'Россия'}
results = {}

for city, country in cities.items():
    if country not in results:
        results[country] = []
    results[country].append(city)

print(results)
```

### **Задача 16. Поиск по вложенности**

**Дано:** У нас есть данные о сервере, где ключи — это ID серверов, а значения — словари с характеристиками.

```python
servers = {
    'srv-1': {'ram': 16, 'status': 'up'},
    'srv-2': {'ram': 8, 'status': 'down'},
    'srv-3': {'ram': 32, 'status': 'up'},
}
```

Выведи названия только тех серверов, у которых статус `'up'` и объем оперативной памяти (`ram`) больше 10 Гб.

**Решение:**

```python
servers = {
    'srv-1': {'ram': 16, 'status': 'up'},
    'srv-2': {'ram': 8, 'status': 'down'},
    'srv-3': {'ram': 32, 'status': 'up'},
}

srv_result = []

for server_name, data in servers.items():
    if data["ram"] > 10 and data["status"] == "up":
        srv_result.append(server_name)

print(srv_result)
```

---