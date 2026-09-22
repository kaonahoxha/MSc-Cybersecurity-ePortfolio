import threading
import unittest
from decimal import Decimal

from bank_account import BankAccount


class TestBankAccountStress(unittest.TestCase):

    def test_100_threads_concurrent_deposits(self):
        account = BankAccount("STRESS-001", Decimal("0.00"))

        def deposit_many_times():
            for _ in range(100):
                account.deposit(Decimal("1.00"))

        threads = [
            threading.Thread(target=deposit_many_times)
            for _ in range(100)
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(
            account.get_balance(),
            Decimal("10000.00")
        )

    def test_100_accounts_with_concurrent_updates(self):
        accounts = [
            BankAccount(
                f"ACC-{number}",
                Decimal("1000.00")
            )
            for number in range(100)
        ]

        def update_account(account):
            for _ in range(100):
                account.deposit(Decimal("5.00"))
                account.withdraw(Decimal("5.00"))

        threads = [
            threading.Thread(
                target=update_account,
                args=(account,)
            )
            for account in accounts
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for account in accounts:
            self.assertEqual(
                account.get_balance(),
                Decimal("1000.00")
            )


if __name__ == "__main__":
    unittest.main()