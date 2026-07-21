educational_grant = int(input("Введите ежемесячную стипендию: "))
expenses = int(input("Введите ежемесячные расходы: "))

total_shortfall = 0
current_expenses = expenses

for i in range(1, 11):
    shortfall = current_expenses - educational_grant
    total_shortfall += shortfall
    print(f"{i} месяц: траты {current_expenses} рублей, не хватает {shortfall} рублей.")
    if i < 10:
        current_expenses = int(current_expenses * 1.03)

print(f"Сумма денег, которую необходимо получить у родителей: {total_shortfall} рублей.")