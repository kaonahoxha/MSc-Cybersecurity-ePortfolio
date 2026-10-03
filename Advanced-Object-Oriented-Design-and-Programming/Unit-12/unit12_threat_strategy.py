from abc import ABC, abstractmethod


class ThreatScoringStrategy(ABC):
    @abstractmethod
    def calculate_score(self, failed_logins, unusual_location):
        pass


class StandardThreatStrategy(ThreatScoringStrategy):
    def calculate_score(self, failed_logins, unusual_location):
        score = failed_logins * 10
        if unusual_location:
            score += 30
        return min(score, 100)


class StrictThreatStrategy(ThreatScoringStrategy):
    def calculate_score(self, failed_logins, unusual_location):
        score = failed_logins * 20
        if unusual_location:
            score += 40
        return min(score, 100)


class ThreatAnalyzer:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def analyse(self, failed_logins, unusual_location):
        return self._strategy.calculate_score(failed_logins, unusual_location)
