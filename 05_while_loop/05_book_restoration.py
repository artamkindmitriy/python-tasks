total_books = int(input("Сколько книг выдал библиотекарь? "))
count = 0
remaining_books = total_books

while remaining_books > 0:
    watched_books = int(input("Сколько книг просмотрено? "))
    if watched_books > total_books:
        print("Нельзя просмотреть больше книг, чем выдано!")
        continue
    restored = int(input("Сколько из них требует реставрации? "))
    count += restored

    if count >= 5:
        print("Ура! Практика завершена!")
        break

    remaining_books -= watched_books

if count < 5:
    print("Цель практики ещё не достигнута — встретимся завтра.")