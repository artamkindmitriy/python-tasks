def palindrome(text):
    return text[::-1] == text
while True:
    text = input("Введите слово: ")
    print(f"Слово является палиндромом" if palindrome(text) else "Слово не является палиндромом")