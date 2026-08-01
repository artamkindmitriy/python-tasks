class SmartDoor:
    def __init__(self, charge):
        self.__is_locked = True
        self.__battery_level = charge

    def lock(self):
        self.__is_locked = True
        print("Дверь заперта.")

    def unlock(self):
        if self.__battery_level > 0:
            print("Дверь открыта")
            self.__is_locked = False
        else:
            print("Батарея разряжена!")

    def charge(self):
        print("Заряжаю батарею...")
        self.__battery_level = 100
        print("Батарея заряжена")

door = SmartDoor(0)

door.unlock()
door.charge()
door.unlock()
door.lock()