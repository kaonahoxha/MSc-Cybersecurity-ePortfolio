class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


account = BankAccount(100)

account.deposit(50)
print("Balance after deposit:", account.get_balance())

account.withdraw(30)
print("Balance after withdrawal:", account.get_balance())
