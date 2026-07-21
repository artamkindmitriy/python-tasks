row = int(input("Введите кол-во рядов: "))
seats = int(input("Введите кол-во сидений в ряде: "))
meters = int(input("Введите кол-во метров между рядами: "))

for i in range(row):
    print("=" * seats + " ", meters * "*" + " ", seats * "=")