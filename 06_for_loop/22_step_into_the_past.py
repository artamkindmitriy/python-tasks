year = int(input("Введите год (не меньше 1900): "))
if year >= 1900:
    for i in range(year, 1898 + 1, -2):
        print(i)
else:
    print("Год должен быть не меньше 1900")