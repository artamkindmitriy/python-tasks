text = input("Строка: ")

tilda_list = []

for index, symbol in enumerate(text):
    if symbol == "~":
        tilda_list.append(index)

tilda_tuple = tuple(tilda_list)

print("Ответ:", *tilda_tuple)