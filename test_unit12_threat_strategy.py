import unittest

from unit12_threat_strategy import (
    StandardThreatStrategy,
    StrictThreatStrategy,
    ThreatAnalyzer,
)


class TestThreatStrategy(unittest.TestCase):

    def test_standard_strategy_calculates_score(self):
        analyzer = ThreatAnalyzer(StandardThreatStrategy())

        result = analyzer.analyse(
            failed_logins=3,
            unusual_location=False
        )

        self.assertEqual(result, 30)

    def test_unusual_location_increases_standard_score(self):
        analyzer = ThreatAnalyzer(StandardThreatStrategy())

        result = analyzer.analyse(
            failed_logins=2,
            unusual_location=True
        )

        self.assertEqual(result, 50)

    def test_strict_strategy_produces_higher_score(self):
        standard = ThreatAnalyzer(StandardThreatStrategy())
        strict = ThreatAnalyzer(StrictThreatStrategy())

        standard_score = standard.analyse(2, True)
        strict_score = strict.analyse(2, True)

        self.assertGreater(strict_score, standard_score)

    def test_strategy_can_be_changed_at_runtime(self):
        analyzer = ThreatAnalyzer(StandardThreatStrategy())

        standard_score = analyzer.analyse(2, True)

        analyzer.set_strategy(StrictThreatStrategy())
        strict_score = analyzer.analyse(2, True)

        self.assertEqual(standard_score, 50)
        self.assertEqual(strict_score, 80)

    def test_score_is_capped_at_100(self):
        analyzer = ThreatAnalyzer(StrictThreatStrategy())

        result = analyzer.analyse(
            failed_logins=10,
            unusual_location=True
        )

        self.assertEqual(result, 100)


if __name__ == "__main__":
    unittest.main()