from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self):
        return sum(product.price for product in self.items)


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid £{amount:.2f} using Credit Card")


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid £{amount:.2f} using PayPal")


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid £{amount:.2f} using Cryptocurrency")


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, order):
        total = order.calculate_total()
        self.payment_method.pay(total)


if __name__ == "__main__":
    order = Order()

    order.add_item(Product("Laptop", 900))
    order.add_item(Product("Mouse", 50))

    payment_method = PayPalPayment()
    processor = PaymentProcessor(payment_method)

    processor.process_payment(order)
