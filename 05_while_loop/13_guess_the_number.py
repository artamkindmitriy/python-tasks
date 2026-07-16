print("Добро пожаловать в игру «Угадай число»!")
print("Загадайте число от 1 до 100. Я буду пытаться его угадать.")

low = 1
high = 100
attempts = 0

while low <= high:
    mid = (low + high) // 2
    attempts += 1

    print(f"Попытка {attempts}. Моё предположение: {mid}")
    print("Ответьте: 1 — равно, 2 — больше, 3 — меньше")

    response = input("Ваш ответ (1/2/3): ").strip()

    if response == '1':
        print(f"Ура! Я угадал ваше число {mid} за {attempts} попыток.")
        break
    elif response == '2':
        low = mid + 1
    elif response == '3':
        high = mid - 1
    else:
        print("Пожалуйста, введите 1, 2 или 3.")
        continue

if low > high:
    print("Что-то пошло не так. Проверьте свои ответы!")