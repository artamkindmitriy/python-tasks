summ = 0
for i in range(5):
    price = float(input("Цена на товар: "))
    summ += price

percent1 = int(input("Повышение на первый год: "))
percent2 = int(input("Повышение на второй год: "))

summ_year0 = summ
summ_year1 = summ * (1 + percent1 / 100)
summ_year2 = summ * (1 + percent2 / 100)

print(f"Сумма цен за каждый год: {summ_year0:.2f} {summ_year1:.2f}  {summ_year2:.2f}")