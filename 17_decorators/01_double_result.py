from functools import wraps

def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value * 2
    return wrapper

@double_result
def test():
    return 2

print(test())