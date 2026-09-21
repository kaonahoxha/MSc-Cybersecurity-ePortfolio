import hashlib
import hmac
import os


class User:
    def __init__(self, username, password_hash, salt, role):
        self.username = username
        self._password_hash = password_hash
        self._salt = salt
        self.role = role

    def verify_password(self, password):
        candidate_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            self._salt,
            100_000
        )
        return hmac.compare_digest(
            self._password_hash,
            candidate_hash
        )


class UserManager:
    VALID_ROLES = {"student", "instructor", "administrator"}

    def __init__(self):
        self._users = {}

    def add_user(self, username, password, role):
        if not username or not username.strip():
            raise ValueError("Username cannot be empty.")

        if username in self._users:
            raise ValueError("Username already exists.")

        if role not in self.VALID_ROLES:
            raise ValueError("Invalid user role.")

        if len(password) < 12:
    raise ValueError(
        "Password must contain at least 12 characters."
        )

        salt = os.urandom(16)
        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt,
            100_000
        )

        user = User(username, password_hash, salt, role)
        self._users[username] = user
        return user

    def authenticate(self, username, password):
        user = self._users.get(username)

        if user is None:
            return False

        return user.verify_password(password)
