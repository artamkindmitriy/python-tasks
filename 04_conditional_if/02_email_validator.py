email = input("Введите email: ")

if "@" in email and email.endswith((".com", ".ru")):
    print("Почта корректна")
else:
    print("Почта неверна")