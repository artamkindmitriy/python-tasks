names = " иван ,  МАРИЯ, петр  "
names_list = names.split(",")

clean_names = []
for name in names_list:
    clean_name = name.strip().capitalize()
    clean_names.append(clean_name)

result = ", ".join(clean_names)

print(f"Результат: {result}")