# MSc Cybersecurity e-Portfolio

## University of Essex Online

Welcome to my MSc Cybersecurity e-Portfolio. This portfolio documents my learning, practical work, skills development and reflections throughout the programme.

## Modules

### Advanced Object-Oriented Design and Programming

This module explores advanced object-oriented programming principles and their application to the design of scalable, maintainable and secure software systems.

**Unit 1 – Introduction and Recap of Object-Oriented Programming**

Unit 1 revisits the core principles of object-oriented programming, including inheritance, polymorphism, abstraction and encapsulation. It also covers classes, objects, constructors, destructors and access control, providing a foundation for more advanced topics later in the module.

### Unit 1 Programming Exercises

- [Task 1 – Basic Class Hierarchy (Inheritance)](unit1_task1.py)
- [Task 2 – Polymorphism with Methods](unit1_task2.py)
- [Task 3 – Encapsulation with Access Control](unit1_task3.py)
- [Task 4 – Abstraction with Base Class](unit1_task4.py)
- [Task 5 – Constructor and Destructor](unit1_task5.py)

## Unit 2 – SOLID Principles of Object-Oriented Design

Unit 2 explores the five SOLID principles of object-oriented design: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation and Dependency Inversion. These principles support the development of maintainable, scalable and adaptable software systems.

### Unit 2 Formative Activity

The formative activity involved refactoring an online shopping system to apply the SOLID principles and improve the structure and maintainability of the code.

- [SOLID Online Shopping System](unit2_solid_shopping_system.py)

## Unit 3 – Design Patterns I: Creational Patterns

Unit 3 introduces creational design patterns and their role in creating flexible and maintainable object-oriented software. The unit covers Singleton, Factory Method, Builder, Prototype and Abstract Factory patterns.

### Unit 3 Formative Activity

The formative activity involved implementing the Factory Method Pattern for a car manufacturing system. The solution uses abstract classes and concrete factories to create Sedan, SUV and Hatchback objects without directly specifying their concrete classes in the client code.

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
