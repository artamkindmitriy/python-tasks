str_input = input("Введите строку: ")

with open("example.txt", "w") as fl:
    try:
        fl.write(str_input)
    except OSError as exc:
        print(f"Проблема при открытии/записи файла:{exc}")
    except ValueError:
        print("Нельзя преобразовать данные в целое")
    except Exception as exc:
        print(f"Неожиданная ошибка:{exc}")

    else:
        print("Все прошло успешно!")
    finally:
        print("Закрытие файла")