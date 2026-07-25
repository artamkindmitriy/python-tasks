small_storage = {
	'гвозди': 5000,
	'шурупы': 3040,
	'саморезы': 2000
}

big_storage = {
	'доски': 1000,
	'балки': 150,
	'рейки': 600
}

combined = small_storage | big_storage

name_tool = input("Введите название товара: ")
result = combined.get(name_tool.lower(), "Такого товара нету на складе")
print(result)