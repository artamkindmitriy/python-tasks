## **Тема: Работа с файлами**

### **Задача 1. Первая запись**

**Дано:** Создайте файл `day_plan.txt`. Запишите в него три дела на сегодня (каждое с новой строки). Выведите содержимое в консоль.

**Решение:**

```python
with open("day_plan.txt", "w") as file:
    file.write("Пропылесосить\nПочитать книгу\nПокодить")

with open("day_plan.txt", "r") as f:
    print(f.read())
```

### **Задача 2. Эхо-чтение**

**Дано:** Напишите программу, которая открывает файл `day_plan.txt` (созданный в первой задаче), читает его содержимое и выводит в консоль каждую строку, добавляя перед ней порядковый номер.

**Решение:**

```python
with open("day_plan.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"{line_number}:{line.rstrip()}")
```

### **Задача 3. Безопасное добавление**

**Дано:** Напишите скрипт, который просит пользователя ввести новую задачу с клавиатуры.

- Если файл `day_plan.txt` уже существует, программа должна **добавить** туда эту задачу в конец.
- Если файла нет, программа должна его создать.

**Решение:**

```python
new_task = input("Введите новую задачу: ")

with open("day_plan.txt", "a") as file:
    file.write(new_task + "\n")

with open("day_plan.txt", "r") as f:
    print("Содержимое файла:")
    print(f.read())
```

### **Задача 4. Интерактивный список покупок**

**Дано:** Создайте скрипт, который запрашивает у пользователя продукты до тех пор, пока он не введет слово «стоп». Каждый введенный продукт записывайте в файл `shopping_list.txt` (каждый с новой строки).

**Решение:**

```python
while True:
    new_product = input("Введите продукт, или 'стоп': ")

    if new_product.lower() == "стоп":
        break
    else:
        with open("shopping_list.txt", "a") as file:
            file.write(new_product + "\n")

with open("shopping_list.txt", "r") as f:
    print("Список покупок:")
    print(f.read())
```

### **Задача 5. Поиск слов в тексте**

**Дано:** Создайте текстовый файл `article.txt` с любым длинным предложением. Напишите программу, которая считает, сколько раз в этом файле встречается определенное слово (слово вводит пользователь).

**Решение:**

```python
search_word = input("Какое слово ищем?: ").lower()

with open("article.txt", "r") as file:
    content = file.read().lower()

    for char in ",.!?":
        content = content.replace(char, " ")

    words = content.split()
    count = words.count(search_word)
print(f"Количество определенных слов:{count}")
```

### **Задача 6. Копирование содержимого**

**Дано:** Создайте текстовый файл `source.txt` и запишите в него любую произвольную строку текста. Напишите программу, которая считывает всё содержимое из `source.txt` и записывает его в новый файл `destination.txt`. После завершения программа должна вывести сообщение об успехе.

**Решение:**

```python
with open("source.txt", "r", encoding="utf-8") as file:
    content = file.read()

with open("destination.txt", "w") as f:
    f.write(content)

with open("destination.txt", "r", encoding="cp1251") as f_read:
    print("Содержание файла destination.txt:")
    print(f_read.read())
```

---