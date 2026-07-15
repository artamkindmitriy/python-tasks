users = ["admin", "guest", "user1"]

user_login = input("Введите логин: ")
user_password = int(input("Введите пароль: "))

if user_login in users:
    if user_password == 12345:
        print("Доступ открыт")
    else:
        print("Неверный пароль")
else:
    print("Пользователь не найден")