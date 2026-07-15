sum_of_buying = int(input("Введите сумму покупки: "))
categoria_of_client = input("Введите категорию клиента: ")

if categoria_of_client.lower() == "vip":
    print("Отлично! Вам дана скидка в 20%")
    print(f"Итоговая сумма: {sum_of_buying * (1 - 0.20)}")
elif categoria_of_client.lower() == "regular":
    print("Прекрасно! Вам дана скидка в 10%")
    print(f"Итоговая сумма: {sum_of_buying * (1 - 0.10)}")
elif categoria_of_client.lower() == "new":
    print("Хорошо! Вам дана скидка в 5%")
    print(f"Итоговая сумма: {sum_of_buying * (1 - 0.05)}")
else:
    print("Неизвестная категория")