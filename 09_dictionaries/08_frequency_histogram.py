from collections import Counter
text = input("Введите текст: ")
counter = Counter(text)
sorted_dict = dict(sorted(counter.items()))
max_count = max(sorted_dict.values())
for symbol, count in sorted_dict.items():
    print(f"{symbol} :{count}")

print(f"Максимальная частота:{max_count}")