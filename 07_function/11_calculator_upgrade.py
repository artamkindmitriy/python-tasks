def calculate():
    n = int(input("Введите число: "))
    choose = int(input("Введите номер действия: "
                       "\n1 - сумма цифр\n"
                       "2 - максимальная цифра\n"
                       "3 - минимальная цифра: \n"))

    if choose == 1:
        choose_1(n)
    elif choose == 2:
        choose_2(n)
    elif choose == 3:
        choose_3(n)
    else:
        print("Введите число: 1, 2 или 3")

def choose_1(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    print(f"Сумма цифр: {total}")

def choose_2(n):
    print(f"Максимальная цифра: {max(str(n))}")

def choose_3(n):
    print(f"Минимальная цифра: {min(str(n))}")

calculate()