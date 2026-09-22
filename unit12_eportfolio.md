# Unit 12 – End of Module e-Portfolio

## Overview

This section of my e-Portfolio brings together practical evidence from the Advanced Object-Oriented Design and Programming module. The artefacts focus on secure and maintainable object-oriented design, design-pattern selection, concurrency, testing, dependency management and architectural adaptability.

The Unit 12 work extends earlier module activities by applying four design patterns to cybersecurity-oriented scenarios and by strengthening the testing and architectural evidence.

---

## 1. Strategy Pattern – Threat Scoring

**Purpose:** Demonstrate interchangeable algorithms and runtime flexibility.

The threat-analysis example separates alternative scoring algorithms from the `ThreatAnalyzer`. Standard and strict strategies can be substituted at runtime without changing the analyzer itself.

**Evidence:**
- [`unit12_threat_strategy.py`](unit12_threat_strategy.py)
- [`test_unit12_threat_strategy.py`](test_unit12_threat_strategy.py)
- [`unit12_threat_strategy.md`](unit12_threat_strategy.md)

**Testing:** 5 tests passed.

**Key trade-off:** Strategy supports changing algorithms and independent testing, but a strategy hierarchy would add unnecessary abstraction if only one stable algorithm existed.

---

## 2. Decorator Pattern – Security Controls

**Purpose:** Demonstrate dynamic extension of behaviour and separation of concerns.

The Decorator artefact adds audit logging and access control around a core security analyzer without modifying its implementation. The decorators can also be composed.

**Evidence:**
- [`unit12_security_decorator.py`](unit12_security_decorator.py)
- [`test_unit12_security_decorator.py`](test_unit12_security_decorator.py)
- [`unit12_security_decorator.md`](unit12_security_decorator.md)

**Testing:** 5 tests passed.

**Key trade-off:** Decorators avoid subclass proliferation and allow flexible composition, but long decorator chains and ordering dependencies can make behaviour harder to trace.

---

## 3. Visitor Pattern – Security Auditing

**Purpose:** Demonstrate separation of algorithms from object structures.

The Visitor artefact applies security checks to servers, databases and user accounts while keeping the auditing operation outside the asset classes.

**Evidence:**
- [`unit12_security_visitor.py`](unit12_security_visitor.py)
- [`test_unit12_security_visitor.py`](test_unit12_security_visitor.py)
- [`unit12_security_visitor.md`](unit12_security_visitor.md)

**Testing:** 6 tests passed.

**Key trade-off:** Visitor makes it easier to introduce new operations when the object structure is stable, but adding new asset types requires corresponding changes to visitor interfaces and implementations.

---

## 4. Abstract Factory – Replaceable Security Services

**Purpose:** Demonstrate creation of interchangeable families of related services.

The Abstract Factory artefact separates the security-analysis platform from concrete local and cloud threat-detection and risk-scoring services.

**Evidence:**
- [`unit12_ai_abstract_factory.py`](unit12_ai_abstract_factory.py)
- [`test_unit12_ai_abstract_factory.py`](test_unit12_ai_abstract_factory.py)
- [`unit12_ai_abstract_factory.md`](unit12_ai_abstract_factory.md)

**Testing:** 3 tests passed.

**Key trade-off:** Abstract Factory supports provider substitution and reduces concrete dependencies, but increases structural complexity and is less attractive where only one fixed service family exists.

The example demonstrates architectural readiness for replaceable AI-oriented services rather than claiming implementation of a production AI model.

---

## 5. Concurrency and Stress Testing

The earlier thread-safe banking artefact was extended with larger stress tests to examine behaviour under greater concurrent workloads.

**Evidence:**
- [`test_unit12_stress.py`](test_unit12_stress.py)
- Unit 6 thread-safe banking implementation and tests

The additional tests include:

- 100 threads each performing 100 deposits, producing 10,000 concurrent deposit operations;
- concurrent repeated updates across 100 separate accounts while checking that balance invariants are preserved.

Both stress tests passed.

These tests provide stronger evidence of concurrent correctness under the tested workload, although they should not be interpreted as a complete performance or production scalability benchmark.

---

## 6. Test-Driven Development

The Unit 10 secure user-management artefact demonstrates test-driven development through test-first implementation and subsequent regression testing.

**Evidence:**
- [`unit10_tdd_elearning.md`](unit10_tdd_elearning.md)
- [`unit10_user_management.py`](unit10_user_management.py)
- [`test_unit10_user_management.py`](test_unit10_user_management.py)

The final suite contains 9 passing tests covering user creation, authentication and password-policy behaviour.

---

## 7. Dependency Injection and Mocking

The Unit 11 artefact demonstrates constructor-based dependency injection by supplying a notification service to `UserManager` rather than constructing a concrete service internally.

**Evidence:**
- [`unit11_dependency_injection.md`](unit11_dependency_injection.md)
- [`unit11_di.py`](unit11_di.py)
- [`test_unit11_di.py`](test_unit11_di.py)

A mock notification service isolates the class under test and verifies the expected interaction without requiring a real external notification provider.

---

## 8. Architecture

The Unit 12 architecture view connects the four design-pattern artefacts conceptually within a modular cybersecurity analysis system.

**Evidence:**
- [`unit12_architecture.md`](unit12_architecture.md)

The diagram illustrates that the patterns address different variation points rather than being interchangeable solutions:

- Strategy – changing algorithms;
- Decorator – optional/composable behaviour;
- Visitor – changing operations over a stable object structure;
- Abstract Factory – interchangeable families of related services.

The diagram is a conceptual integration of the portfolio artefacts rather than a claim that the individual examples form a production-ready platform.

---

## 9. Assessment Traceability

A separate traceability map links the practical evidence to the learning areas and assessment requirements.

**Evidence:**
- [`unit12_traceability.md`](unit12_traceability.md)

This makes the relationship between implementation, testing, architectural decisions and learning outcomes explicit.

---

## Reflection

The portfolio demonstrates progression from implementing individual object-oriented concepts towards evaluating when particular abstractions are justified. A recurring lesson is that using more patterns does not automatically improve a design. Strategy, Decorator, Visitor and Abstract Factory address different forms of change, and their value depends on whether those variation points genuinely exist.

Testing also progressed from verifying expected outputs towards examining dependency isolation, edge cases, concurrent behaviour and larger workloads. However, passing tests provide evidence only for the scenarios exercised; they do not by themselves establish production security, scalability or reliability.

The strongest architectural improvement across the module has therefore been not simply adding abstraction, but learning to balance extensibility, testability and separation of concerns against complexity and overengineering.
