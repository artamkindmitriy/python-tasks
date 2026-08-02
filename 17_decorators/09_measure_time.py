import time

def measure_time(func):
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        print(f"Метод {func.__name__} выполнился за {end_time - start_time:.4f} сек")
        return result
    return wrapper

class Tester:
    @measure_time
    def test(self):
        time.sleep(1)
        return "Успех"

obj = Tester()
obj.test()