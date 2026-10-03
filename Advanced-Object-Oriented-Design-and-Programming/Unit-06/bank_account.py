import threading
from decimal import Decimal, InvalidOperation
from typing import Union


Number = Union[int, float, str, Decimal]


class BankAccount:
    """
    Represents a thread-safe bank account.

    Each account owns an independent lock so that operations affecting
    different accounts can still run concurrently. Monetary values are
    stored using Decimal to avoid floating-point rounding problems.
    """

    def __init__(self, account_number: str, initial_balance: Number = 0):
        if not account_number:
            raise ValueError("Account number cannot be empty.")

        balance = self._to_decimal(initial_balance)

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_number = account_number
        self._balance = balance
        self._lock = threading.Lock()

    @staticmethod
    def _to_decimal(amount: Number) -> Decimal:
        """
        Convert a monetary value safely to Decimal.
        """
        try:
            return Decimal(str(amount))
        except (InvalidOperation, ValueError, TypeError) as exc:
            raise ValueError("Amount must be a valid number.") from exc

    def deposit(self, amount: Number) -> Decimal:
        """
        Deposit a positive amount into the account.
        """
        amount = self._to_decimal(amount)

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        with self._lock:
            self._balance += amount
            return self._balance

    def withdraw(self, amount: Number) -> bool:
        """
        Withdraw money if sufficient funds are available.
        """
        amount = self._to_decimal(amount)

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        with self._lock:
            if amount > self._balance:
                return False

            self._balance -= amount
            return True

    def get_balance(self) -> Decimal:
        """
        Return the current balance using the account lock.
        """
        with self._lock:
            return self._balance

    def transfer_to(
        self,
        destination_account: "BankAccount",
        amount: Number
    ) -> bool:
        """
        Transfer money safely between two accounts.

        Both account locks are acquired in a deterministic order.
        This prevents opposite-direction transfers from creating
        a circular wait and therefore reduces the risk of deadlock.
        """
        if not isinstance(destination_account, BankAccount):
            raise TypeError("Destination must be a BankAccount.")

        if destination_account is self:
            raise ValueError("Cannot transfer to the same account.")

        amount = self._to_decimal(amount)

        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        # Always acquire the two locks in the same deterministic order.
        # The object ID acts as a secondary key if account numbers match.
        first, second = sorted(
            (self, destination_account),
            key=lambda account: (
                str(account.account_number),
                id(account)
            )
        )

        with first._lock:
            with second._lock:
                if amount > self._balance:
                    return False

                self._balance -= amount
                destination_account._balance += amount

                return True


# Temporary manual check.
# Formal automated testing is performed separately in test_banking.py.
if __name__ == "__main__":
    account_a = BankAccount("ACC001", "1000.00")
    account_b = BankAccount("ACC002", "500.00")

    account_a.deposit("200.00")
    account_a.withdraw("100.00")
    account_a.transfer_to(account_b, "250.00")

    print("Account A:", account_a.get_balance())
    print("Account B:", account_b.get_balance())
