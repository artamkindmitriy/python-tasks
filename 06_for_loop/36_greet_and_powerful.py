text = input("Введите текст: ")

words = text.split()

count_letter = 0

for i in words:
    if len(i) > count_letter:
        count_letter = len(i)

print("Самое длинное слово,", count_letter, "букв")