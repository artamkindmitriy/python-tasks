search_word = input("Какое слово ищем?: ").lower()

with open("article.txt", "r") as file:
    content = file.read().lower()

    for char in ",.!?":
        content = content.replace(char, " ")

    words = content.split()
    count = words.count(search_word)
print(f"Количество определенных слов:{count}")