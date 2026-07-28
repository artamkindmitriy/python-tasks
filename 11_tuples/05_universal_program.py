def return_list(iterable):
    return list(iterable[::2])

str_1 = "О Дивный Новый мир!"
print(f"Результат:{return_list(str_1)}")
str_2 = [100, 200, 300, 'буква', 0, 2, 'a']
print(f"Результат:{return_list(str_2)}")