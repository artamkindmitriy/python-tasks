input_string = input("Введите строку: ")

first_h_index = input_string.find('h')

last_h_index = input_string.rfind('h')

substring_between_h = input_string[first_h_index + 1:last_h_index]

reversed_substring = substring_between_h[::-1]

result = reversed_substring

print("Развёрнутая последовательность между первым и последним h:", result)