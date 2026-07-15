food = "молоко, хлеб, сыр, колбаса"

food_list = [item.strip() for item in food.split(",")]

if len(food_list) > 5:
    print("Слишком много покупок, удаляю лишнее!")
    food_list.pop()
elif len(food_list) < 2:
    print("Маловато покупок, добавь что-нибудь!")
elif 2 <= len(food_list) <= 5:
    print("Отличный список!")

food_list.sort()
print(f"Итоговый список: {food_list}")