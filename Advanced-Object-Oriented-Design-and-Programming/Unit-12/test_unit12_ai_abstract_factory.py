import unittest

from unit12_ai_abstract_factory import (
    LocalSecurityFactory,
    CloudSecurityFactory,
    SecurityAnalysisPlatform,
)


class TestSecurityServiceFactories(unittest.TestCase):

    def test_local_factory_creates_compatible_services(self):
        platform = SecurityAnalysisPlatform(LocalSecurityFactory())

        result = platform.analyse("login-event")

        self.assertEqual(
            result["detection"],
            "Local detector analysed: login-event"
        )
        self.assertEqual(
            result["risk"],
            "Local risk score generated for: login-event"
        )

    def test_cloud_factory_creates_compatible_services(self):
        platform = SecurityAnalysisPlatform(CloudSecurityFactory())

        result = platform.analyse("network-traffic")

        self.assertEqual(
            result["detection"],
            "Cloud detector analysed: network-traffic"
        )
        self.assertEqual(
            result["risk"],
            "Cloud risk score generated for: network-traffic"
        )

    def test_provider_family_can_be_switched(self):
        local_platform = SecurityAnalysisPlatform(LocalSecurityFactory())
        cloud_platform = SecurityAnalysisPlatform(CloudSecurityFactory())

        local_result = local_platform.analyse("suspicious-event")
        cloud_result = cloud_platform.analyse("suspicious-event")

        self.assertIn("Local", local_result["detection"])
        self.assertIn("Cloud", cloud_result["detection"])
        self.assertNotEqual(
            local_result["detection"],
            cloud_result["detection"]
        )


if __name__ == "__main__":
    unittest.main()