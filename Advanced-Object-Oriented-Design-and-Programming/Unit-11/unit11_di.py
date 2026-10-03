from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def send_notification(self, user, message):
        pass


class EmailService(NotificationService):

    def send_notification(self, user, message):
        print(f"Sending email to {user}: {message}")


class SMSService(NotificationService):

    def send_notification(self, user, message):
        print(f"Sending SMS to {user}: {message}")


class UserManager:

    def __init__(self, notifier):
        self.notifier = notifier

    def register_user(self, user):
        self.notifier.send_notification(user, "Welcome!")
