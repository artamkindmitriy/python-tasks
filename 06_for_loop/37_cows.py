stalls = input("Введите 10 стойл в одну строку. a — свободное стойло, b — занятое: ")

total_milk = 0
current_stall_milk = 2

for i in range(len(stalls)):
    if stalls[i] == 'b':
        total_milk += current_stall_milk
    elif stalls[i] != 'a':
        print("Ошибка: используйте только 'a' или 'b'!")
        break
    current_stall_milk += 2

print("Произведено молока за день:", total_milk)