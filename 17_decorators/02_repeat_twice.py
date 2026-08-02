from functools import wraps

def repeat_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@repeat_twice
def say_hi():
    print("Привет!")

say_hi()

# Вызов say_hi() должен напечатать "Привет!" два раза.