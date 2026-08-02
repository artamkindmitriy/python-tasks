from functools import wraps

def check_access(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role != "admin":
                raise PermissionError("Ошибка: нет прав")
            else:
                print("Доступ разрешен")
                return func(*args, **kwargs)
        return wrapper
    return decorator

@check_access("admin")
def test_check_is_admin():
    pass

test_check_is_admin()