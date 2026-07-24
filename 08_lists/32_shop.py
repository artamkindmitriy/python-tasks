original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

for number in range(len(original_prices)):
    if original_prices[number] < 0:
        original_prices[number] = 0

print(f"Результат: {original_prices}")