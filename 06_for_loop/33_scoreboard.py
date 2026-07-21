number = int(input("Введите число: "))
print("-=-", end=" ")

for i in range(0, number + 1, 10):
    if number >= 0:
        print(i, end=" -=- ")
    else:
        break