num = int(input("Введите целое число: "))
dict_numbers = {i: i ** 2 for i in range(1, num + 1)}

print(f"Результат:{dict_numbers}")