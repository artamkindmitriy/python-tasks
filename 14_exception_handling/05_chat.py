chat_file = "chat.txt"

def show_chat():
    with open(chat_file, "a+", encoding='utf-8') as f:
        f.seek(0)
        print(f.read())

def send_message(user):
    msg = input("Введите сообщение: ")
    with open(chat_file, 'a', encoding='utf-8') as f:
        f.write(f"{user}:{msg}\n")
    print("Сообщение отправлено")

def main():
    user = input("Введите имя: ")
    while True:
        print("\n1. Посмотреть чат\n2. Отправить сообщение")
        choice = input("Выберите действие: ")
        if choice == "1":
            show_chat()
        elif choice == "2":
            send_message(user)
        else:
            print("Некорректный выбор")

if __name__ == "__main__":
    main()