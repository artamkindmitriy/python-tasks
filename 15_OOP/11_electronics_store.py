class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class Smartphone(Device):
    def __init__(self, brand, price, operating_system):
        super().__init__(brand, price)
        self.operating_system = operating_system

    def call(self):
        pass

class Laptop(Device):
    def __init__(self, brand, price, ram_size):
        super().__init__(brand, price)
        self.ram_size = ram_size

    def run_program(self):
        pass

laptop = Laptop("Apple", 100000, 1000)
smartphone = Smartphone("Samsung", 10000, "iOS")

print(isinstance(laptop, Laptop))
print(isinstance(smartphone, Smartphone))
print()

print(issubclass(Laptop, Device))
print(issubclass(Smartphone, Device))