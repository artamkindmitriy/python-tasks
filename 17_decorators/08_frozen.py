def frozen(cls):
    def add_method(self, name, value):
        if hasattr(self, name):
            object.__setattr__(self, name, value)
        else:
            raise AttributeError(f"Нельзя добавлять новые атрибуты: {name}")

    cls.__setattr__ = add_method
    return cls