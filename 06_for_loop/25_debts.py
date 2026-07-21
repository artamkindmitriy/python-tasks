count_debtors = int(input("Введите количество должников: "))
summ = 0

for debtor in range(0, count_debtors, 5):
    print(f"Должник с номером {debtor}")
    count_money = int(input("Сколько должен? "))
    summ += count_money

print(f"Общая сумма долга: {summ}")