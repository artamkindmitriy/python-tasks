x, y = 7, 10

width, height = 20, 15

print("Марсоход находится на позиции", x, y, ", введите команду: ")

while True:
    command = input().upper()

    if command == "W" and y < height:
        y += 1
    elif command == "S" and y > 1:
        y -= 1
    elif command == "A" and x > 1:
        x -= 1
    elif command == "D" and x < width:
        x += 1

    print("Марсоход находится на позиции", x, y, ", введите команду:")