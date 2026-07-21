right_word = "Карамба"

count = 0

for i in range(10):
    quest = input("Введите кодовое слово: ")
    if quest == right_word:
        count += 1

print("Общее кол-во попавших на борт:", count)