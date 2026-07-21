first_step = int(input("Введите первый член прогрессии: "))
second_step = int(input("Введите разность: "))

print(first_step, end=".")
last_sum = first_step
for i in range(2):
    first_step += second_step
    last_sum += first_step
    print(first_step, end=".")
print(last_sum)