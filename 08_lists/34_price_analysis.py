import random

original_prices = []
for i in range(10):
    price = random.randint(-50, 100)
    original_prices.append(price)

new_prices = []

for price in original_prices:
    new_prices.append(price)

for i in range(len(new_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))