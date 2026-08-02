from functools import wraps

is_authenticated = True

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            return "Доступ запрещён"
    return wrapper

@require_auth
def get_secret_data():
    return "Секретный документ: 12345"

print(get_secret_data())