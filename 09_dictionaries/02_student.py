information = input("Введите информацию о студенте через пробел\n"
                    " (имя, фамилия, город, место учёбы, оценки): ")

dict_inf = {}

words = information.split()

dict_inf["Имя"] = words[0]
dict_inf["Фамилия"] = words[1]
dict_inf["Город"] = words[2]
dict_inf["Место учёбы"] = words[3]
dict_inf["Оценки"] = [int(x) for x in words[4:]]

print()

for key, value in dict_inf.items():
    print(f"{key} -{value}")