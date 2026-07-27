text = input("Введите строку: ")
diff_numbers = set()

for char in text:
    if char.isdigit():
        diff_numbers.add(char)

print(f"Различные цифры строки: {"".join(sorted(diff_numbers))}")