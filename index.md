# MSc Cybersecurity e-Portfolio

## University of Essex Online

Welcome to my MSc Cybersecurity e-Portfolio. This portfolio documents my learning, practical work, skills development and reflections throughout the programme.

## Modules

### Security and Risk Management

This module examines qualitative and quantitative risk assessment, threat modelling, security standards, business continuity and disaster recovery.

- [Security and Risk Management Module Portfolio](security-risk-management.md)

---

# Advanced Object-Oriented Design and Programming

This module developed my understanding of advanced object-oriented programming and its application to maintainable, secure, testable and scalable software systems. The portfolio includes practical programming exercises, automated testing, design-pattern implementations, concurrency work, dependency injection, architectural evaluation and requirements traceability.

## Unit 1 – Introduction and Recap of Object-Oriented Programming

Unit 1 revisited the fundamental principles of object-oriented programming, including inheritance, polymorphism, abstraction and encapsulation, together with classes, objects, constructors, destructors and access control.

### Practical Evidence

- [Task 1 – Basic Class Hierarchy](unit1_task1.py)
- [Task 2 – Polymorphism](unit1_task2.py)
- [Task 3 – Encapsulation](unit1_task3.py)
- [Task 4 – Abstraction](unit1_task4.py)
- [Task 5 – Constructor and Destructor](unit1_task5.py)

## Unit 2 – SOLID Principles of Object-Oriented Design

Unit 2 explored the Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation and Dependency Inversion principles. The work demonstrated how responsibilities and dependencies can be structured to improve maintainability and extensibility.

### Practical Evidence

- [SOLID Online Shopping System](unit2_solid_shopping_system.py)

## Unit 3 – Creational Design Patterns

Unit 3 introduced creational design patterns, including Singleton, Factory Method, Builder, Prototype and Abstract Factory. The practical work demonstrated how object creation can be separated from client code.

### Practical Evidence

- [Factory Method Car Manufacturing System](unit3_factory_method.py)

## Unit 4 – Structural Design Patterns

Unit 4 explored Adapter, Bridge, Composite, Decorator, Facade, Proxy and Flyweight patterns and their role in composing flexible object structures.

The practical exercise applied the Decorator Pattern to extend behaviour dynamically without modifying the underlying component.

### Practical Evidence

- [Decorator Pattern – Coffee Ordering System](unit4_decorator_pattern.py)

## Unit 5 – Behavioural Design Patterns

Unit 5 explored Strategy, Observer, Chain of Responsibility, Template Method, Command and State patterns.

The practical exercise applied Strategy to interchangeable payment behaviours, separating individual payment algorithms from the main processing context.

### Practical Evidence

- [Strategy Pattern – Payment Processing System](unit5_strategy_pattern.py)

## Unit 6 – Concurrency and Parallelism

Unit 6 explored threads, processes, shared mutable state, race conditions, synchronisation and deadlock prevention.

The banking artefact applied per-account locking to protect balance-changing operations and deterministic lock ordering to reduce circular-wait risk during transfers. Later stress testing extended this work to larger concurrent workloads.

### Practical Evidence

- [Thread-Safe Banking System](bank_account.py)
- [Concurrency Stress Tests](test_unit12_stress.py)

## Unit 8 – Refactoring and Code Smells

Unit 8 developed my understanding of refactoring as controlled structural improvement rather than simply increasing abstraction. The unit considered code smells, maintainability, magic numbers, long methods and the use of patterns such as Strategy where genuine variation exists.

The principles from this unit informed the later capstone work, particularly the evaluation of whether additional abstraction was justified by a real source of change.

## Unit 9 – Object-Oriented Software Architecture

Unit 9 extended object-oriented reasoning from individual classes to software architecture. The unit considered layered architectures, monolithic and distributed systems, dependency management, data access and the trade-offs associated with architectural complexity.

These concepts informed the integrated architecture developed in the final portfolio and the evaluation of scalability, maintainability and dependency boundaries.

## Unit 10 – Test-Driven Development and Unit Testing

Unit 10 applied the Red-Green-Refactor cycle to secure user-management functionality. Tests were used to specify and verify registration, authentication and password-policy behaviour while the implementation incorporated defensive validation and secure password handling.

### Practical Evidence

- [TDD User Management Documentation](unit10_tdd_elearning.md)
- [User Management Implementation](unit10_user_management.py)
- [TDD Automated Tests](test_unit10_user_management.py)

## Unit 11 – Dependency Injection and Inversion of Control

Unit 11 explored dependency injection and inversion of control as mechanisms for reducing coupling and improving testability.

Constructor injection was used to supply a notification dependency to the user-management component. Mocking then allowed the expected interaction to be tested without contacting an external notification provider.

### Practical Evidence

- [Dependency Injection Documentation](unit11_dependency_injection.md)
- [Dependency Injection Implementation](unit11_di.py)
- [DI and Mocking Tests](test_unit11_di.py)

---

# Unit 12 – Capstone and Final e-Portfolio

Unit 12 brought together the module learning through cybersecurity-oriented implementations of advanced design patterns, concurrency testing, architectural evaluation and requirements traceability.

## Strategy Pattern – Threat Analysis

The Strategy Pattern was applied to interchangeable cybersecurity threat-scoring algorithms. This demonstrates runtime behavioural flexibility while keeping the analysis context independent of individual scoring policies.

### Evidence

- [Strategy Documentation](unit12_threat_strategy.md)
- [Strategy Implementation](unit12_threat_strategy.py)
- [Strategy Tests](test_unit12_threat_strategy.py)

## Decorator Pattern – Composable Security Controls

The Decorator Pattern was used to compose access-control and audit-logging behaviour around a core security analyser while preserving the underlying interface.

### Evidence

- [Decorator Documentation](unit12_security_decorator.md)
- [Decorator Implementation](unit12_security_decorator.py)
- [Decorator Tests](test_unit12_security_decorator.py)

## Visitor Pattern – Security Auditing

The Visitor Pattern separates security-audit operations from the assets being inspected, demonstrating the trade-off between extending operations and extending the object structure.

### Evidence

- [Visitor Documentation](unit12_security_visitor.md)
- [Visitor Implementation](unit12_security_visitor.py)
- [Visitor Tests](test_unit12_security_visitor.py)

## Abstract Factory – Replaceable Security-Service Families

The Abstract Factory implementation models related local and cloud security-service families. It demonstrates how client code can depend on stable abstractions rather than provider-specific implementations.

The exercise also provides architectural context for future AI or data-science integrations in which external providers may need to be replaced without changing consuming application logic.

### Evidence

- [Abstract Factory Documentation](unit12_ai_abstract_factory.md)
- [Abstract Factory Implementation](unit12_ai_abstract_factory.py)
- [Abstract Factory Tests](test_unit12_ai_abstract_factory.py)

## Concurrency Stress Testing

The Unit 6 banking work was extended with larger concurrent workloads to provide stronger evidence of thread-safe behaviour under the tested conditions.

- [Thread-Safe Banking System](bank_account.py)
- [Concurrency Stress Tests](test_unit12_stress.py)

## Integrated Architecture

The final architecture considers how Strategy, Decorator, Visitor and Abstract Factory can coexist because each addresses a different source of variation. The architecture is evaluated in terms of extensibility, maintainability, testability, security and the risk of unnecessary abstraction.

- [Integrated Architecture](unit12_architecture.md)

## Requirements–Design–Test Traceability

A traceability artefact connects requirements with corresponding design decisions and testing evidence, making the relationship between intended behaviour, implementation and verification explicit.

- [Requirements–Design–Test Traceability](unit12_traceability.md)

## Final e-Portfolio Evidence

The consolidated e-Portfolio documents the final artefacts, their purpose, implementation evidence and critical evaluation.

- [Final Unit 12 e-Portfolio](unit12_eportfolio.md)

---

# End of Module Assignment Evidence

This repository provides the supporting evidence referenced in my Advanced Object-Oriented Design and Programming End of Module Assignment, including:

- object-oriented programming exercises;
- SOLID and design-pattern implementations;
- thread-safe banking and concurrency stress testing;
- TDD and automated unit testing;
- dependency injection and mocking;
- Strategy, Decorator, Visitor and Abstract Factory implementations;
- cybersecurity-oriented architectural integration;
- requirements–design–test traceability; and
- critical documentation accompanying the final e-Portfolio.

The artefacts represent academic and practical learning evidence rather than production-ready systems.
