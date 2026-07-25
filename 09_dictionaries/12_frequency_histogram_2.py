def main():
    text = input("Введите текст: ")

    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    inverted_dict = {}
    for char, count in freq_dict.items():
        if count not in inverted_dict:
            inverted_dict[count] = []
        inverted_dict[count].append(char)

    print("\nОригинальный словарь частот:")
    for char in sorted(freq_dict.keys()):
        print(f"{char} :{freq_dict[char]}")

    print("\nИнвертированный словарь частот:")
    for count in sorted(inverted_dict.keys()):
        sorted_chars = sorted(inverted_dict[count])
        print(f"{count} :{sorted_chars}")

if __name__ == "__main__":
    main()