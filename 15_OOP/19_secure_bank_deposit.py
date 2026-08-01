class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Ты не можешь установить баланс меньше нуля")
        elif abs(value - self._balance) > 1_000_000:
            raise ValueError("Старая сумма не может отличаться от новой на 1_000_000 рублей")

        self._balance = value