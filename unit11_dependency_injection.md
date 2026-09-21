# Unit 11 – Dependency Injection and Inversion of Control

This activity demonstrates how Dependency Injection (DI) can reduce tight coupling and improve testability.

In the original design, UserManager creates EmailService directly. This means UserManager depends on a specific notification implementation. I refactored the design so that a notification service is supplied to UserManager instead. This allows alternative services, such as SMS notifications, to be introduced without modifying UserManager and enables mock services to be used during unit testing.
