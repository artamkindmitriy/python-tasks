fruits = "  apple, banana, cherry  "

new_fruits = [f.strip() for f in fruits.split(",")]

if "banana" in new_fruits:
    print("Бананы на месте!")
else:
    new_fruits.append("banana")

print(f"Итоговый список: {' | '.join(new_fruits)}")