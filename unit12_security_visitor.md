# Unit 12 – Visitor Pattern: Security Audit

## Overview

This artefact demonstrates the Visitor design pattern through a simple cybersecurity auditing scenario. The system contains different asset types (`Server`, `Database`, and `UserAccount`) while the `SecurityAuditVisitor` performs security checks on each asset.

## Why Visitor?

The Visitor pattern separates the security-audit operation from the asset classes themselves. This means additional operations, such as compliance reporting or risk scoring, could be introduced as new visitors without placing those responsibilities inside each asset class.

This separation supports maintainability and the Single Responsibility Principle because the asset classes represent system resources while the visitor contains the auditing logic.

## Testing

The implementation is supported by six unit tests covering:

- patched and unpatched servers;
- encrypted and unencrypted databases;
- user accounts with and without MFA.

All six tests pass successfully.

## Critical Reflection

Visitor is useful when the set of asset types is relatively stable but new operations need to be added. For example, the same assets could later support security auditing, compliance reporting and risk assessment through separate visitors.

However, the pattern introduces additional abstraction. It also becomes less flexible when new asset types are added because the visitor interface and its implementations must be updated. For a very small system with only one simple operation, this additional structure could therefore be unnecessary.

## Files

- `unit12_security_visitor.py` – Visitor pattern implementation.
- `test_unit12_security_visitor.py` – unit tests for the security audit visitor.
