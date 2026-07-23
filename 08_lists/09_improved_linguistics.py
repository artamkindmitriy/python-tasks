word1 = input("Введите 1 слово: ")
word2 = input("Введите 2 слово: ")
word3 = input("Введите 3 слово: ")

count1, count2, count3 = 0, 0, 0

while True:
    word = input("Слово из текста: ")
    if word == "end":
        break

    if word == word1:
        count1 += 1
    if word == word2:
        count2 += 1
    if word == word3:
        count3 += 1

print("Подсчёт слов в тексте")
print(f"{word1}: {count1}")
print(f"{word2}: {count2}")
print(f"{word3}: {count3}")