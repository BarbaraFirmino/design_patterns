from abc import abstractmethod

class ShoppingCart():
    def __init__(self) -> None:
        pass

    def pay(self, payment_strategy):
        payment_strategy.pay()

class PaymentStrategy():
    @abstractmethod
    def pay(self):
        pass

class CreditCard(PaymentStrategy):
    def __init__(self, card_number, cvv) -> None:
        self.card_number = card_number
        self.cvv = cvv
    def pay(self):
        print("Pagando com cartão de crédito", self.card_number)

class Pix(PaymentStrategy):
    def __init__(self, pix_key) -> None:
        self.pix_key = pix_key
    def pay(self):
        print("Pagando com cartão de pix", self.pix_key)


card = CreditCard("0123", "123")
pix = Pix("bgfaraujo@gmail.com")

list_payment = [card, pix]

cart = ShoppingCart()

for payment in list_payment:
    cart.pay(payment)