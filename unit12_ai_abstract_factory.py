from abc import ABC, abstractmethod


class ThreatDetector(ABC):
    """Interface for threat detection services."""

    @abstractmethod
    def detect(self, data):
        pass


class RiskScorer(ABC):
    """Interface for risk scoring services."""

    @abstractmethod
    def score(self, data):
        pass


class LocalThreatDetector(ThreatDetector):
    def detect(self, data):
        return f"Local detector analysed: {data}"


class LocalRiskScorer(RiskScorer):
    def score(self, data):
        return f"Local risk score generated for: {data}"


class CloudThreatDetector(ThreatDetector):
    def detect(self, data):
        return f"Cloud detector analysed: {data}"


class CloudRiskScorer(RiskScorer):
    def score(self, data):
        return f"Cloud risk score generated for: {data}"


class SecurityServiceFactory(ABC):
    """Factory interface for creating related security services."""

    @abstractmethod
    def create_threat_detector(self):
        pass

    @abstractmethod
    def create_risk_scorer(self):
        pass


class LocalSecurityFactory(SecurityServiceFactory):
    def create_threat_detector(self):
        return LocalThreatDetector()

    def create_risk_scorer(self):
        return LocalRiskScorer()


class CloudSecurityFactory(SecurityServiceFactory):
    def create_threat_detector(self):
        return CloudThreatDetector()

    def create_risk_scorer(self):
        return CloudRiskScorer()


class SecurityAnalysisPlatform:
    """Uses a family of services without depending on concrete providers."""

    def __init__(self, factory):
        self.detector = factory.create_threat_detector()
        self.risk_scorer = factory.create_risk_scorer()

    def analyse(self, data):
        return {
            "detection": self.detector.detect(data),
            "risk": self.risk_scorer.score(data),
        }