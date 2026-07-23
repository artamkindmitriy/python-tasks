films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

current_films = []

while True:
    print(f"Ваш текущий список фильмов: {current_films}")
    film = input("Название фильма: ")
    print("Команды: добавить, вставить, удалить, выход")
    command = input("Введите команду: ")

    if command.lower() == "добавить":
        if film in films:
            if film in current_films:
                print("Этот фильм уже есть в вашем списке.")
            else:
                current_films.append(film)
        else:
            print("Такого фильма нету в списке.")

    elif command.lower() == "вставить":
        insert_choose = int(input("На какое место (позицию) вставить фильм? "))
        if film in films:
            if film in current_films:
                print("Этот фильм уже есть в вашем списке.")
            else:
                current_films.insert(insert_choose - 1, film)
                print(f"Фильм '{film}' добавлен в ваш список на позицию {insert_choose}")
        else:
            print("Такого фильма нету в списке.")

    elif command.lower() == "удалить":
        if film in films:
            if film in current_films:
                current_films.remove(film)
            else:
                print("Этого фильма нету в списке")
        else:
            print("Такого фильма нету в списке.")

    elif command.lower() == "выход":
        print("До свидания!")
        break

    else:
        print("Неверная команда")

    print()