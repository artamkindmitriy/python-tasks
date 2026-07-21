reverse_timer = int(input("Введите время для обратного отсчёта (в секундах): "))
print(f"Таймер установлен на {reverse_timer} секунд.")

for second in range(reverse_timer, 0, -1):
    print(f"Осталось {second} секунд")
    question = int(input("Введите 1, если еда готова, или 0, чтобы продолжить: "))
    if question == 1:
        print(f"Ваша еда готова, можете забрать! Таймер был прерван на {second} секундах.")
        break
    elif question == 0:
        continue

    else:
        print("Выберете 1 или 0")
        continue

else:
    print("Ваша еда готова. Осторожно, горячо!")