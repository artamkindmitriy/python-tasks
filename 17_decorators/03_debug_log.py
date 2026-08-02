from functools import wraps

def debug_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@debug_log
def test(a, b):
    return a + b

result = test(3, 5)
print(f"Результат: {result}")
print(f"Имя функции: {test.__name__}")
print(f"Докстринг: {test.__doc__}")