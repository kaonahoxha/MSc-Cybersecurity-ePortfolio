import unittest

from unit12_security_decorator import (
    BasicSecurityAnalyzer,
    AuditLoggingDecorator,
    AccessControlDecorator,
)


class TestSecurityDecorator(unittest.TestCase):

    def test_basic_analyzer(self):
        analyzer = BasicSecurityAnalyzer()

        result = analyzer.analyse("failed-login")

        self.assertEqual(
            result,
            "Analysed security event: failed-login"
        )

    def test_audit_logging_decorator_adds_log(self):
        audit_log = []
        analyzer = AuditLoggingDecorator(
            BasicSecurityAnalyzer(),
            audit_log
        )

        result = analyzer.analyse("malware-alert")

        self.assertEqual(
            result,
            "Analysed security event: malware-alert"
        )
        self.assertEqual(
            audit_log,
            ["Audit: malware-alert"]
        )

    def test_authorised_user_can_analyse_event(self):
        analyzer = AccessControlDecorator(
            BasicSecurityAnalyzer(),
            authorised=True
        )

        result = analyzer.analyse("network-alert")

        self.assertEqual(
            result,
            "Analysed security event: network-alert"
        )

    def test_unauthorised_user_is_blocked(self):
        analyzer = AccessControlDecorator(
            BasicSecurityAnalyzer(),
            authorised=False
        )

        with self.assertRaises(PermissionError):
            analyzer.analyse("sensitive-event")

    def test_decorators_can_be_combined(self):
        audit_log = []

        analyzer = AccessControlDecorator(
            AuditLoggingDecorator(
                BasicSecurityAnalyzer(),
                audit_log
            ),
            authorised=True
        )

        result = analyzer.analyse("suspicious-login")

        self.assertEqual(
            result,
            "Analysed security event: suspicious-login"
        )
        self.assertEqual(
            audit_log,
            ["Audit: suspicious-login"]
        )


if __name__ == "__main__":
    unittest.main()