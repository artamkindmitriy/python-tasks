import random

russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

list_letters_1 = [random.choice(russian_alphabet) for _ in range(10)]
list_letters_2 = [random.choice(russian_alphabet) for _ in range(10)]

print(f"Первый список:{list_letters_1}")
print(f"Второй список:{list_letters_2}")

dict_letters_1 = dict(enumerate(list_letters_1))
dict_letters_2 = dict(enumerate(list_letters_2))

print()

print(f"Первый словарь:{dict_letters_1}")
print(f"Второй словарь:{dict_letters_2}")