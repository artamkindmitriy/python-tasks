class PaymentSystem:
    def process_payment(self, amount):
        pass

class CreditCard(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата {amount} руб. картой через терминал")

class PayPal(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата {amount} руб. через PayPal-аккаунт")