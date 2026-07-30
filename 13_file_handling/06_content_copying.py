with open("source.txt", "r", encoding="utf-8") as file:
    content = file.read()

with open("destination.txt", "w") as f:
    f.write(content)

with open("destination.txt", "r", encoding="cp1251") as f_read:
    print("Содержание файла destination.txt:")
    print(f_read.read())