class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной!")

        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Недостаточно средств.")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной!")

        self.__balance -= amount

    def get_balance(self):
        return f"Текущее состояние баланса: {self.__balance}"

account = BankAccount()
account.deposit(1000)
print(account.get_balance())  # Выведет: 1000

account.withdraw(500)
print(account.get_balance())  # Выведет: 500

account.withdraw(2000)  # Выведет сообщение о нехватке средств