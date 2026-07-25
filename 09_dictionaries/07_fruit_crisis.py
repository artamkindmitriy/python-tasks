incomes = {
	'apple': 5600.20,
	'orange': 3500.45,
	'banana': 5000.00,
	'bergamot': 3700.56,
	'durian': 5987.23,
	'grapefruit': 300.40,
	'peach': 10000.50,
	'pear': 1020.00,
	'persimmon': 310.00,
}

total_income = sum(incomes.values())

min_val = min(incomes.values())
min_product = min(incomes, key=incomes.get)

print(f"Общий доход за год составил{total_income} рублей")
print(f"Самый маленький доход у{min_product}. Он составляет{min_val} рублей")

incomes.pop(min_product)

print(f"Итоговый словарь:{incomes}")