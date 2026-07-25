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