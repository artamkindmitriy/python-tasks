from functools import wraps

def multiply(factor):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return factor * func(*args, **kwargs)
        return wrapper
    return decorator

@multiply(3)
def check():
    return 10

print(check())