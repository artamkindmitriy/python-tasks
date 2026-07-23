N = int(input("Кол-во пакетов: "))

all_package = []

count_error = 0
count_lost_package = 0

for package in range(1, N + 1):
    print(f"Пакет номер {package}")
    current_package = []
    for n_bit in range(1, 5):
        bit = int(input(f"{n_bit} бит: "))
        current_package.append(bit)
    errors = current_package.count(-1)

    if errors > 1:
        count_lost_package += 1
        print("Много ошибок в пакете")

    elif errors <= 1:
        count_error += errors
        all_package.extend(current_package)

    print()

print(f"Полученное сообщение: {all_package}")
print(f"Кол-во ошибок в сообщении: {count_error}")
print(f"Кол-во потерянных пакетов: {count_lost_package}")