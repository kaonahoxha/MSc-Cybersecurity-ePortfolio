import unittest

from unit10_user_management import User, UserManager


class TestUserManagement(unittest.TestCase):

    def setUp(self):
        self.manager = UserManager()

    def test_add_valid_user(self):
        user = self.manager.add_user(
            "student1",
            "SecurePass123!",
            "student"
        )

        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "student1")
        self.assertEqual(user.role, "student")

    def test_duplicate_username_rejected(self):
        self.manager.add_user(
            "student1",
            "SecurePass123!",
            "student"
        )

        with self.assertRaises(ValueError):
            self.manager.add_user(
                "student1",
                "AnotherPass123!",
                "student"
            )

    def test_invalid_role_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_user(
                "student1",
                "SecurePass123!",
                "superuser"
            )

    def test_weak_password_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_user(
                "student1",
                "123",
                "student"
            )

    def test_authentication_success(self):
        self.manager.add_user(
            "student1",
            "SecurePass123!",
            "student"
        )

        self.assertTrue(
            self.manager.authenticate(
                "student1",
                "SecurePass123!"
            )
        )

    def test_authentication_wrong_password(self):
        self.manager.add_user(
            "student1",
            "SecurePass123!",
            "student"
        )

        self.assertFalse(
            self.manager.authenticate(
                "student1",
                "WrongPassword123!"
            )
        )
    def test_password_requires_uppercase(self):
        with self.assertRaises(ValueError):
            self.manager.add_user(
                "student1",
                "securepass123!",
                "student"
            )

    def test_password_requires_number(self):
        with self.assertRaises(ValueError):
            self.manager.add_user(
                "student1",
                "SecurePassword!",
                "student"
            )

    def test_password_requires_special_character(self):
        with self.assertRaises(ValueError):
            self.manager.add_user(
                "student1",
                "SecurePass123",
                "student"
            )

if __name__ == "__main__":
    unittest.main()
