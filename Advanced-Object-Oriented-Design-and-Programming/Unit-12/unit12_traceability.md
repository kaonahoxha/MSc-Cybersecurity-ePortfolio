# Unit 12 – Assessment Traceability Map

This traceability map links the module learning outcomes and End of Module Assignment requirements to practical evidence in my e-Portfolio.

| Learning Area / Requirement | Practical Evidence | What the Evidence Demonstrates |
|---|---|---|
| Secure coding | Unit 10 secure user management; Unit 12 Decorator | Password protection, validation, access control, audit logging and separation of security responsibilities |
| Advanced OOP | Visitor, Strategy, Decorator and Abstract Factory artefacts | Abstraction, inheritance, polymorphism, encapsulation and interface-based design |
| Strategy Pattern | `unit12_threat_strategy.py` | Interchangeable threat-scoring algorithms and runtime behavioural flexibility |
| Decorator Pattern | `unit12_security_decorator.py` | Dynamic addition and composition of audit logging and access-control behaviour |
| Visitor Pattern | `unit12_security_visitor.py` | Separation of security-audit operations from system asset structures |
| Abstract Factory Pattern | `unit12_ai_abstract_factory.py` | Creation and substitution of related local/cloud security-service families |
| Concurrency and robustness | Unit 6 banking artefact; `test_unit12_stress.py` | Thread safety, synchronisation, balance invariants and larger-scale concurrent testing |
| Test-Driven Development | Unit 10 user-management artefact | Incremental test-first development and regression testing |
| Dependency Injection | Unit 11 DI artefact | Reduced coupling and substitution of notification-service dependencies |
| Mocking | Unit 11 DI tests | Isolation of dependencies and verification of interactions without a real external service |
| Scalability testing | `test_unit12_stress.py` | 10,000 concurrent deposit operations and concurrent updates across 100 accounts |
| AI-oriented adaptability | Unit 12 Abstract Factory | Replaceable service families illustrating architectural readiness for changing AI/security providers |
| Maintainability and extensibility | Pattern artefacts and accompanying reflections | Evaluation of when abstraction supports change and when patterns may introduce unnecessary complexity |
| Testing quality | Unit 10, Unit 11 and Unit 12 test suites | Behavioural verification, edge cases, isolation and regression protection |
| Critical evaluation | Unit 12 pattern documentation | Explicit limitations, design trade-offs and alternatives rather than pattern description alone |

## Evidence Summary

The portfolio demonstrates progression from individual object-oriented and concurrency concepts towards more modular and replaceable architectures. The artefacts are not intended to represent production-scale systems; instead, they provide focused evidence of specific design decisions and their consequences.

The pattern implementations deliberately use cybersecurity-oriented scenarios so that design-pattern knowledge is applied within the wider MSc Cyber Security context. Testing accompanies each Unit 12 implementation so that the portfolio demonstrates behaviour rather than relying only on code examples.

The traceability map also identifies limitations in the evidence. The AI-oriented Abstract Factory demonstrates architectural adaptability rather than a deployed AI model, while the concurrency stress tests provide stronger workload evidence without constituting a full performance benchmark.
