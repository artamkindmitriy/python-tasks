cwk = int(input("Кол-во сотрудников в офисе: "))

id_cwk = []

for person in range(cwk):
    id_person = int(input("ID сотрудника: "))
    id_cwk.append(id_person)

find_id_cwk = int(input("Какой ID ищем? "))

if find_id_cwk not in id_cwk:
    print("Сотрудник не работает!")
else:
    print("Сотрудник на месте")