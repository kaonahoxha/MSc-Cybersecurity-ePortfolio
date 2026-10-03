from abc import ABC, abstractmethod


class SystemAsset(ABC):
    """Base class for assets that can be inspected by a visitor."""

    @abstractmethod
    def accept(self, visitor):
        pass


class Server(SystemAsset):
    def __init__(self, hostname, patched):
        self.hostname = hostname
        self.patched = patched

    def accept(self, visitor):
        return visitor.visit_server(self)


class Database(SystemAsset):
    def __init__(self, name, encrypted):
        self.name = name
        self.encrypted = encrypted

    def accept(self, visitor):
        return visitor.visit_database(self)


class UserAccount(SystemAsset):
    def __init__(self, username, mfa_enabled):
        self.username = username
        self.mfa_enabled = mfa_enabled

    def accept(self, visitor):
        return visitor.visit_user_account(self)


class AssetVisitor(ABC):
    """Defines operations supported for each system asset."""

    @abstractmethod
    def visit_server(self, server):
        pass

    @abstractmethod
    def visit_database(self, database):
        pass

    @abstractmethod
    def visit_user_account(self, account):
        pass


class SecurityAuditVisitor(AssetVisitor):
    """Performs security checks without changing the asset classes."""

    def visit_server(self, server):
        if not server.patched:
            return f"{server.hostname}: server requires patching"
        return f"{server.hostname}: no patching issue detected"

    def visit_database(self, database):
        if not database.encrypted:
            return f"{database.name}: database encryption is required"
        return f"{database.name}: encryption enabled"

    def visit_user_account(self, account):
        if not account.mfa_enabled:
            return f"{account.username}: MFA is not enabled"
        return f"{account.username}: MFA enabled"