def test(n):
    if n >= 0:
        positive()
    else:
        negative()

def positive():
    print("Это положительное число")

def negative():
    print("Это отрицательное число")

n = int(input("Введите число: "))
test(n)