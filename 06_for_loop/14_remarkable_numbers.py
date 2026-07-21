print("Замечательные числа в диапазоне двузначных:")

for i in range(10, 100):
    first_s = i // 10
    second_s = i % 10

    result = first_s * second_s * 3

    if i == result:
        print(i)