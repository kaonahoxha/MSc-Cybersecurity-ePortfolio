# MSc Cybersecurity e-Portfolio

## University of Essex Online

Welcome to my MSc Cybersecurity e-Portfolio. This portfolio documents my learning, practical work, skills development and reflections throughout the programme.

## Modules

### Security and Risk Management

This module examines qualitative and quantitative risk assessment, threat modelling, security standards, business continuity and disaster recovery.

- [Security and Risk Management module portfolio](security-risk-management.md)

---

# Advanced Object-Oriented Design and Programming

This module explores advanced object-oriented programming principles and their application to the design of scalable, maintainable, testable and secure software systems.

## Unit 1 – Introduction and Recap of Object-Oriented Programming

Unit 1 revisited inheritance, polymorphism, abstraction, encapsulation, classes, objects, constructors, destructors and access control.

### Programming Exercises

- [Task 1 – Basic Class Hierarchy](unit1_task1.py)
- [Task 2 – Polymorphism](unit1_task2.py)
- [Task 3 – Encapsulation](unit1_task3.py)
- [Task 4 – Abstraction](unit1_task4.py)
- [Task 5 – Constructor and Destructor](unit1_task5.py)

## Unit 2 – SOLID Principles

Unit 2 explored the Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation and Dependency Inversion principles and their role in maintainable and adaptable OO systems.

### Practical Evidence

- [SOLID Online Shopping System](unit2_solid_shopping_system.py)

## Unit 3 – Creational Design Patterns

Unit 3 introduced Singleton, Factory Method, Builder, Prototype and Abstract Factory patterns.

### Practical Evidence

- [Factory Method Car Manufacturing System](unit3_factory_method.py)

## Unit 4 – Structural Design Patterns

Unit 4 explored Adapter, Bridge, Composite, Decorator, Facade, Proxy and Flyweight patterns.

### Practical Evidence

- [Decorator Pattern – Coffee Ordering System](unit4_decorator_pattern.py)

## Unit 5 – Behavioural Design Patterns

Unit 5 explored Strategy, Observer, Chain of Responsibility, Template Method, Command and State patterns.

### Practical Evidence

- [Strategy Pattern – Payment Processing System](unit5_strategy_pattern.py)

## Unit 6 – Concurrency and Parallelism

Unit 6 explored threads, shared mutable state, race conditions, synchronisation and deadlock prevention. The practical work developed a thread-safe banking system using per-account locking and deterministic lock ordering for transfers.

### Practical Evidence

- [Thread-Safe Banking System](bank_account.py)
- [Banking System Tests](test_bank_account.py)
- [Concurrency Stress Tests](test_unit12_stress.py)

---

# Final AOODP e-Portfolio Evidence

The later portfolio work brings together secure coding, concurrency, testing, dependency management, advanced design patterns and architectural evaluation.

## Unit 10 – Test-Driven Development

The secure user-management artefact applies TDD to registration, authentication and password-policy requirements.

- [TDD User Management](unit10_tdd_elearning.md)
- [TDD Automated Tests](test_unit10_user_management.py)

## Unit 11 – Dependency Injection and Mocking

Dependency injection was used to separate user-management logic from an external notification dependency, enabling deterministic testing through mocking.

- [Dependency Injection and Mocking](unit11_dependency_injection.md)
- [DI and Mocking Tests](test_unit11_di.py)

## Unit 12 – Capstone and Integrated Architecture

Unit 12 integrates advanced design patterns, concurrency testing and architectural evaluation within cybersecurity-oriented examples.

### Strategy Pattern
- [Strategy Documentation](unit12_threat_strategy.md)
- [Strategy Tests](test_unit12_threat_strategy.py)

### Decorator Pattern
- [Decorator Documentation](unit12_security_decorator.md)
- [Decorator Tests](test_unit12_security_decorator.py)

### Visitor Pattern
- [Visitor Documentation](unit12_security_visitor.md)
- [Visitor Tests](test_unit12_security_visitor.py)

### Abstract Factory
- [Abstract Factory Documentation](unit12_ai_abstract_factory.md)
- [Abstract Factory Tests](test_unit12_ai_abstract_factory.py)

### Concurrency, Architecture and Traceability
- [Concurrency Stress Tests](test_unit12_stress.py)
- [Integrated Architecture](unit12_architecture.md)
- [Requirements–Design–Test Traceability](unit12_traceability.md)
- [Final e-Portfolio Evidence](unit12_eportfolio.md)

---

## End of Module Assignment Evidence

The repository contains the source code, automated tests, stress tests, architecture documentation and requirements–design–test traceability evidence referenced in my Advanced Object-Oriented Design and Programming End of Module Assignment.
- [Factory Method Car Manufacturing System](unit3_factory_method.py)


## Unit 4 – Design Patterns II: Structural Patterns

Unit 4 focused on structural design patterns and how they can be used to organise classes and objects into flexible and maintainable software structures. I explored the Adapter, Bridge, Composite, Decorator, Facade, Proxy and Flyweight patterns.

### Unit 4 Practical Exercise

For the practical activity, I implemented the Decorator Pattern using a simple coffee ordering system. The program demonstrates how additional features, such as milk and sugar, can be added dynamically without changing the original coffee class.

- [Decorator Pattern – Coffee Ordering System](unit4_decorator_pattern.py)

### Collaborative Discussion

I also explored the Adapter, Bridge and Composite patterns through practical scenarios and Python examples as part of the collaborative discussion.


## Unit 5 – Design Patterns III: Behavioural Patterns

Unit 5 focused on behavioural design patterns and how they manage communication and interaction between objects. The unit covered Strategy, Observer, Chain of Responsibility, Template Method, Command and State patterns.

### Unit 5 Practical Exercise

For the practical activity, I implemented the Strategy Pattern using a payment processing system. Different payment methods were separated into individual strategies, allowing the payment behaviour to be changed without modifying the main PaymentProcessor class.

The implementation demonstrates how Credit Card, PayPal and Bank Transfer payment strategies can be used interchangeably at runtime, making the system easier to extend and maintain.

- [Strategy Pattern – Payment Processing System](https://github.com/kaonahoxha/MSc-Cybersecurity-ePortfolio/blob/main/unit5_strategy_pattern.py)

### Collaborative Discussion 2

As part of the collaborative discussion, I analysed an initially tightly coupled payment processing system and considered how the Strategy Pattern could improve its design. The refactored approach separates payment-specific behaviour from the main processor, improving extensibility, maintainability and testability.

---

## Final AOODP e-Portfolio

The later units brought the module concepts together through secure coding, testing, dependency management, design patterns, concurrency and architectural evaluation.

### Unit 10 – Test-Driven Development
- [TDD User Management](unit10_tdd_elearning.md)

### Unit 11 – Dependency Injection and Mocking
- [Dependency Injection and Mocking](unit11_dependency_injection.md)

### Unit 12 – Capstone and Integrated Architecture
- [Strategy Pattern](unit12_threat_strategy.md)
- [Decorator Pattern](unit12_security_decorator.md)
- [Visitor Pattern](unit12_security_visitor.md)
- [Abstract Factory](unit12_ai_abstract_factory.md)
- [Concurrency Stress Tests](test_unit12_stress.py)
- [Integrated Architecture](unit12_architecture.md)
- [Requirements–Design–Test Traceability](unit12_traceability.md)
- [Final e-Portfolio Evidence](unit12_eportfolio.md)
