time_visiting = int(input("Время визита: "))
is_pass = input("Есть пропуск (True/False)? ") == "True"
is_dressing = input("Есть защитный халат (True/False)? ") == "True"

if 9 <= time_visiting <= 24 and is_pass and is_dressing:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")