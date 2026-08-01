class ManagePassword:
    def __init__(self, password):
        if len(password) < 8:
            raise ValueError("Минимальная длина пароля - 8 символов.")

        self.__current_password = password

    def change_password(self, old_password, new_password):
        if old_password != self.__current_password:
            raise ValueError("Вы ввели неверный пароль.")

        if len(new_password) >= 8:
            print("Смена пароля успешна!")
            self.__current_password = new_password
        else:
            raise ValueError("Новый пароль не может быть короче 8 символов.")

    def get_password_masked(self):
        return "*" * len(self.__current_password)