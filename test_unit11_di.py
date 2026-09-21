import unittest
from unittest.mock import Mock

from unit11_di import UserManager, NotificationService


class TestUserManager(unittest.TestCase):

    def test_register_user_sends_welcome_notification(self):
        mock_notifier = Mock(spec=NotificationService)
        manager = UserManager(mock_notifier)

        manager.register_user("student1")

        mock_notifier.send_notification.assert_called_once_with(
            "student1",
            "Welcome!"
        )


if __name__ == "__main__":
    unittest.main()
