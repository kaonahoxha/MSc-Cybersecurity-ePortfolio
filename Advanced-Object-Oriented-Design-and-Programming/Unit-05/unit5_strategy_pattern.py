from abc import ABC, abstractmethod


# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Credit card payment authorised: ${amount:.2f}")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"PayPal payment authorised: ${amount:.2f}")


class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Bank transfer initiated: ${amount:.2f}")


# Context
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be positive")

        self.strategy.pay(amount)


# Demonstration
processor = PaymentProcessor(CreditCardPayment())
processor.process_payment(120)

processor.set_strategy(PayPalPayment())
processor.process_payment(75)

processor.set_strategy(BankTransferPayment())
processor.process_payment(250)
