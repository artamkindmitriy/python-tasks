import math

size_ai_layer = float(input("Введите размерность нейронного слоя: "))

print(f"Отсечение хвоста тензора: {math.floor(size_ai_layer)}")
print(f"Резервированная память: {math.ceil(size_ai_layer)}")