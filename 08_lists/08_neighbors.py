s = input("Введите строку: ")
n = int(input("Номер символа: "))

if 1 <= n <= len(s):
    target = s[n - 1]
    left = s[n - 2] if n > 1 else None
    right = s[n] if n < len(s) else None
    if left:
        print(f"Символ слева: {left}")
    else:
        print("Символа слева нет")

    if right:
        print(f"Символ справа: {right}")
    else:
        print("Символа справа нет")

    count = (left == target) + (right == target)

    if count == 0:
        print("Таких же символов нет")
    elif count == 1:
        print("Есть ровно один такой же символ")
    else:
        print("Есть два таких же символа")
else:
    print("Ошибка: номер символа вне диапазона!")