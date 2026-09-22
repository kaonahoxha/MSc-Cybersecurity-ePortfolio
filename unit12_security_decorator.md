# Unit 12 – Decorator Pattern: Security Controls

## Overview

This artefact demonstrates the Decorator design pattern by adding security-related behaviour to a basic security analysis service without modifying its original implementation.

The `BasicSecurityAnalyzer` provides the core analysis operation. Two decorators extend this behaviour:

- `AuditLoggingDecorator` records analysed security events.
- `AccessControlDecorator` checks authorisation before allowing analysis.

The decorators can also be combined around the same analyzer.

## Why Decorator?

Decorator was selected because logging and access control are additional responsibilities rather than part of the core analysis logic. Wrapping the analyzer allows these behaviours to be introduced dynamically while preserving the same `SecurityAnalyzer` interface.

This approach supports separation of concerns and avoids creating multiple subclasses for every possible combination of security features.

## Testing

Five unit tests verify:

- the basic analyzer operates independently;
- audit logging is added correctly;
- authorised access is permitted;
- unauthorised access raises a `PermissionError`;
- multiple decorators can be combined successfully.

All five tests pass successfully.

## Critical Reflection

Decorator provides flexibility because security behaviours can be composed according to the requirements of a particular deployment. For example, audit logging can be applied independently or combined with access control without changing `BasicSecurityAnalyzer`.

The pattern also supports the Open/Closed Principle because new behaviour can be introduced through additional decorators rather than repeatedly modifying the core class.

However, extensive decorator chains can make execution flow harder to understand and debug. The order of decorators may also affect behaviour. For example, placing audit logging outside an access-control decorator could record attempted access that is ultimately rejected, whereas placing it inside may only record authorised analysis. This ordering therefore needs to be an explicit design decision in a production security system.

For a small application with fixed behaviour, separate decorators could introduce unnecessary abstraction.

## Files

- `unit12_security_decorator.py` – Decorator pattern implementation.
- `test_unit12_security_decorator.py` – unit tests covering individual and combined decorators.
