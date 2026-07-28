data = {
    (5000, 123456): ('Иванов', 'Василий'),

    (6000, 111111): ('Иванов', 'Петр'),

    (7000, 222222): ('Медведев', 'Алексей'),

    (8000, 333333): ('Алексеев', 'Георгий'),

    (9000, 444444): ('Георгиева', 'Мария')
}

def get_information(seria_passport, num_passport):
    result = data.get((seria_passport, num_passport), "Паспорт не найден")

    print(result)

s_passport = int(input("Введите серию паспорта: "))
n_passport = int(input("Введите номер паспорта: "))

get_information(seria_passport=s_passport, num_passport=n_passport)