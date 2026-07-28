import random

numbers_tuple_1 = tuple(random.randint(0, 5) for _ in range(10))
numbers_tuple_2 = tuple(random.randint(-5, 0) for _  in range(10))

mixed_tuple = numbers_tuple_1 + numbers_tuple_2
print(f"Третий кортеж:{mixed_tuple}")
print(f"Количество нулей в нём:{mixed_tuple.count(0)}")