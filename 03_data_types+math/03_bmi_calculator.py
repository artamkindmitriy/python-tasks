meters = float(input("Введите рост: "))
weight = float(input("Введите вес: "))

index_of_body = round(weight / (meters ** 2), 2)

if index_of_body <= 18.5:
    print("Это недобор!")
elif index_of_body <= 25:
    print("Это норма")
elif index_of_body <= 30:
    print("Это избыток!")
else:
    print("У вас ожирение!")