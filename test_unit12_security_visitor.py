import unittest

from unit12_security_visitor import (
    Server,
    Database,
    UserAccount,
    SecurityAuditVisitor,
)


class TestSecurityAuditVisitor(unittest.TestCase):

    def setUp(self):
        self.visitor = SecurityAuditVisitor()

    def test_unpatched_server_is_identified(self):
        server = Server("web-01", patched=False)

        result = server.accept(self.visitor)

        self.assertEqual(
            result,
            "web-01: server requires patching"
        )

    def test_patched_server_passes_check(self):
        server = Server("web-01", patched=True)

        result = server.accept(self.visitor)

        self.assertEqual(
            result,
            "web-01: no patching issue detected"
        )

    def test_unencrypted_database_is_identified(self):
        database = Database("customer-db", encrypted=False)

        result = database.accept(self.visitor)

        self.assertEqual(
            result,
            "customer-db: database encryption is required"
        )

    def test_encrypted_database_passes_check(self):
        database = Database("customer-db", encrypted=True)

        result = database.accept(self.visitor)

        self.assertEqual(
            result,
            "customer-db: encryption enabled"
        )

    def test_account_without_mfa_is_identified(self):
        account = UserAccount("student1", mfa_enabled=False)

        result = account.accept(self.visitor)

        self.assertEqual(
            result,
            "student1: MFA is not enabled"
        )

    def test_account_with_mfa_passes_check(self):
        account = UserAccount("student1", mfa_enabled=True)

        result = account.accept(self.visitor)

        self.assertEqual(
            result,
            "student1: MFA enabled"
        )


if __name__ == "__main__":
    unittest.main()