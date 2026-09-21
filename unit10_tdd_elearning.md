# Unit 10 – Test-Driven Development: Secure E-Learning Platform

## Task 1: Software Architecture

### Architecture Choice

For the secure e-learning platform, I selected a layered architecture consisting of a Presentation Layer, Business Logic Layer and Data Access Layer.

This architecture provides clear separation of responsibilities. The Presentation Layer handles interaction with students, instructors and administrators. The Business Logic Layer manages functionality such as authentication, course management and enrolment, while the Data Access Layer manages the storage and retrieval of system data.

I selected this approach because separating responsibilities improves maintainability and allows individual parts of the application to be modified with less impact on the rest of the system. It also supports security by preventing the presentation layer from directly accessing stored user and course data.

A microservices architecture could provide greater independent scalability for a much larger platform, but it would also introduce additional complexity in deployment, communication and security. For the scope of this system, layered architecture provides an appropriate balance between scalability, maintainability and security (Chow, 2024).
