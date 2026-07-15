user_name = input("Введите имя: ")
user_age = int(input("Введите возраст: "))

if user_name.lower() == "Admin":
    print("Привет, босс!")
elif user_age < 18:
    print(f"Привет, {user_name}! Тебе еще рано сюда.")
else:
    print(f"Привет, {user_name}")