def generate_list():
    return [[row * 4 + col for col in range(1, 4) for row in range(4)]]

result = generate_list()
print(result)