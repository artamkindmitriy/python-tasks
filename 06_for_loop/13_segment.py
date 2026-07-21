a = int(input("Начало отрезка: "))
b = int(input("Конец отрезка: "))

sum_multiples = 0
count_multiples = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum_multiples += i
        count_multiples += 1

print("Числа из отрезка, которые делятся на 3: ")
for i in range(a, b + 1):
    if i % 3 == 0:
        print(i)

if count_multiples > 0:
    avg = sum_multiples / count_multiples
    print(f"Средняя арифметическое этих чисел: {avg}")
else:
    print("В заданном отрезке нет чисел, кратных 3.")