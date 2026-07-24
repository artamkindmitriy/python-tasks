text = input("Введите текст: ")
vowels_list = []
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

for vowel in text:
    if vowel in vowels:
        vowels_list.append(vowel)

print(f"Список гласных букв: {vowels_list}")
print(f"Длина списка: {len(vowels_list)}")