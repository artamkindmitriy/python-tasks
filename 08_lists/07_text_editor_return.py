S = input("Введите строку: ")
count_change = 0

new_s = []

for char in S:
    if char == ":":
        new_s.append(";")
        count_change += 1
    else:
        new_s.append(char)

result = "".join(new_s)
print(f"Исправленная строка: {result}")
print(f"Кол-во замен: {count_change}")