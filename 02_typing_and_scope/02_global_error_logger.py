error_count = 0

def register_error():
    global error_count
    error_count += 1

    return error_count

register_error()
register_error()
print(f"Значение функции: {register_error()}")