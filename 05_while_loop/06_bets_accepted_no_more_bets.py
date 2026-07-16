money = int(input("Введите кол-во денег: "))

while money < 10000:
    dropped_number = int(input("Сколько выпало на кубике? "))
    if dropped_number == 3:
        print("Вы проиграли всё!")
        money = 0
        break
    else:
        print("Вы выиграли 500 рублей!")
        money += 500
print("Игра закончена.")
print("Итого осталось:", money)