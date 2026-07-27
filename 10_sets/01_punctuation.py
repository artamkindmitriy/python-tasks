text = input("Введите строку: ")
symbols = set()
special_symbols = ".,;:!?"

for char in text:
    if char in special_symbols:
        symbols.add(char)

print(f"Различные знаки пунктуации: {" ".join(symbols)}")
print(f"Количество различных знаков пунктуации:{len(symbols)}")