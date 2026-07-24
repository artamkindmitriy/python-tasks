n = int(input("Количество чисел: "))
seq = []
for _ in range(n):
    num = int(input("Число: "))
    seq.append(num)

print(f"Последовательность: {seq}")

max_palindrome_length = 0
for L in range(n, 0, -1):
    suffix = seq[-L:]
    if suffix == suffix[::-1]:
        max_palindrome_length = L
        break

count_to_add = n - max_palindrome_length

numbers_to_add = seq[:count_to_add][::-1]

print(f"Нужно приписать чисел: {count_to_add}")
print(f"Сами числа: {numbers_to_add}")