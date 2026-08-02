def debug_init(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"Создан объект класса {cls.__name__}")
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@debug_init
class Unit:
    def __init__(self, name):
        self.name = name

u1 = Unit("Воин")
u2 = Unit("Лучник")