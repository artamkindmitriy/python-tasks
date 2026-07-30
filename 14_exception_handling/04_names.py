total = 0

with open("people.txt", encoding='utf-8') as f:
    for i, name in enumerate(f, 1):
        name = name.strip()
        if len(name) < 3:
            raise ValueError(f"Строка{i}: '{name}' < 3 символов")
        total += len(name)

print(total)