nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))

    nums_list.append(num)

print(f'Максимальное число в списке: {max(nums_list)}')

print(f'Минимальное число в списке: {min(nums_list)}')