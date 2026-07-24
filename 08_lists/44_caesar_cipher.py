def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if 'а' <= char <= 'я':
            shifted = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            encrypted_text += shifted
        elif 'А' <= char <= 'Я':
            shifted = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            encrypted_text += shifted
        else:
            encrypted_text += char

    return encrypted_text

message = input("Введите сообщение: ")
shift_value = int(input("Введите сдвиг: "))

encrypted_message = caesar_cipher(message, shift_value)

print("Зашифрованное сообщение:", encrypted_message)