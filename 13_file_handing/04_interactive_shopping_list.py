while True:
    new_product = input("Введите продукт, или 'стоп': ")

    if new_product.lower() == "стоп":
        break
    else:
        with open("shopping_list.txt", "a") as file:
            file.write(new_product + "\n")

with open("shopping_list.txt", "r") as f:
    print("Список покупок:")
    print(f.read())