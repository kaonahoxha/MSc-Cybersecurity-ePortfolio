from abc import ABC, abstractmethod


class SecurityAnalyzer(ABC):
    """Interface for security analysis services."""

    @abstractmethod
    def analyse(self, event):
        pass


class BasicSecurityAnalyzer(SecurityAnalyzer):
    """Performs the core security analysis."""

    def analyse(self, event):
        return f"Analysed security event: {event}"


class SecurityAnalyzerDecorator(SecurityAnalyzer):
    """Base decorator wrapping another security analyzer."""

    def __init__(self, analyzer):
        self._analyzer = analyzer

    def analyse(self, event):
        return self._analyzer.analyse(event)


class AuditLoggingDecorator(SecurityAnalyzerDecorator):
    """Adds audit logging without modifying the wrapped analyzer."""

    def __init__(self, analyzer, audit_log):
        super().__init__(analyzer)
        self.audit_log = audit_log

    def analyse(self, event):
        result = super().analyse(event)
        self.audit_log.append(f"Audit: {event}")
        return result


class AccessControlDecorator(SecurityAnalyzerDecorator):
    """Adds an authorisation check before analysis."""

    def __init__(self, analyzer, authorised):
        super().__init__(analyzer)
        self.authorised = authorised

    def analyse(self, event):
        if not self.authorised:
            raise PermissionError("Access denied")

        return super().analyse(event)