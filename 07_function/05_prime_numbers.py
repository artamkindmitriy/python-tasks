def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

n = int(input("Введите количество чисел в последовательности: "))
count = 0
for i in range(n):
    new_number = int(input("Введите число: "))
    if is_prime(new_number):
        count += 1

print(count)