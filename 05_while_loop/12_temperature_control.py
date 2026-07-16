print("Программа для отслеживания температуры")

bag_count = 0
degrees = []

while True:
    degree = int(input("Какая температура на датчике? "))

    if degree in degrees:
        print(f"Внимание: дублирующее значение температуры {degree} обнаружено!")
        bag_count += 1
        print(f"Зафиксировано сбоев датчика: {bag_count}")
        question = int(input("Хотите продолжить сбор данных? 1 — да, 0 — нет: "))
        if question == 0:
            print("Сбор данных остановлен")
            break
        else:
            continue

    degrees.append(degree)