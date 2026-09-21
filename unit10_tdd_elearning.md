# Unit 10 – Test-Driven Development: Secure E-Learning Platform

## Task 1: Software Architecture

### Architecture Choice

For the secure e-learning platform, I selected a layered architecture consisting of a Presentation Layer, Business Logic Layer and Data Access Layer.

This architecture provides clear separation of responsibilities. The Presentation Layer handles interaction with students, instructors and administrators. The Business Logic Layer manages functionality such as authentication, course management and enrolment, while the Data Access Layer manages the storage and retrieval of system data.

I selected this approach because separating responsibilities improves maintainability and allows individual parts of the application to be modified with less impact on the rest of the system. It also supports security by preventing the presentation layer from directly accessing stored user and course data.

A microservices architecture could provide greater independent scalability for a much larger platform, but it would also introduce additional complexity in deployment, communication and security. For the scope of this system, layered architecture provides an appropriate balance between scalability, maintainability and security (Chow, 2024).

### High-Level Architecture

The platform is divided into three layers:

Presentation Layer  
↓  
- Student Interface
- Instructor Interface
- Administrator Interface

Business Logic Layer  
↓  
- User Management
- Course Management
- Enrolment Management
- Authentication

Data Access Layer  
↓  
- User Repository
- Course Repository
- Enrolment Repository
- Database

This separation ensures that users interact with the system through the presentation layer rather than accessing stored data directly. Business rules and security controls are handled within the business logic layer, while database operations remain isolated within the data access layer.

### Security Considerations

Security is particularly important because the platform handles user credentials, personal information and course data. The design will include the following controls:

- **Authentication:** Users must authenticate before accessing protected functionality. Different roles, such as student, instructor and administrator, should only access functions appropriate to their role.
- **Password Security:** Passwords should never be stored in plaintext. A secure password-hashing algorithm should be used before credentials are stored.
- **Input Validation:** User input should be validated before processing or storage to reduce the risk of invalid or malicious data entering the system.
- **Access Control:** Authorisation checks should ensure that authenticated users cannot perform actions outside their permitted role.
- **Data Protection:** Sensitive information should be protected during transmission and when stored.
- **Error Handling:** Errors should be handled without exposing sensitive internal information to users.

These controls follow the secure coding principles considered earlier in the module and allow security responsibilities to remain separated from the presentation layer.

## Task 2: Implementation and Test-Driven Development

The User Management module was developed using Test-Driven Development (TDD). I created the unit tests before implementing the User and UserManager classes. The initial tests defined the expected behaviour for user registration, duplicate usernames, role validation, password validation and authentication.

After defining the tests, I implemented the minimum functionality required to satisfy them. Passwords are not stored in plaintext. Instead, PBKDF2-HMAC with a unique random salt is used for password hashing, and secure comparison is used during authentication.

## Task 3: Testing and Validation

The completed implementation was tested using Python's unittest framework. Six unit tests were executed covering:

- Valid user registration
- Duplicate username rejection
- Invalid role rejection
- Weak password rejection
- Successful authentication
- Incorrect password authentication

All six tests passed successfully.
