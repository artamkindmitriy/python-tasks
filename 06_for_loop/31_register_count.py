text = input("Введите текст: ")

symbol1 = "Ы"
symbol2 = "ы"

count_s1 = 0
count_s2 = 0

for i in text:
    if symbol1 in i:
        count_s1 += 1
    elif symbol2 in i:
        count_s2 += 1
    else:
        pass

print(f"Больших букв Ы: {count_s1}")
print(f"Маленьких букв Ы: {count_s2}")