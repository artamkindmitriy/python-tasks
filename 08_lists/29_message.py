text = input("Введите строку: ")
symbol = input("Введите дополнительный символ: ")

list_text = []
list_symbol = []

for sym in text:
    list_text.append(sym * 2)

for sym_symbol in symbol:
    for sym_text in list_text:
        list_symbol.append(sym_text + symbol)

print(f"Список удвоенных символов: {list_text}")
print(f"Склейка с дополнительным символом: {list_symbol}")