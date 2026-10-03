# Unit 12 – Abstract Factory: AI Security Services

## Overview

This artefact demonstrates the Abstract Factory design pattern through a security analysis platform. The platform can use different families of related services without depending directly on their concrete implementations.

Two service families are provided:

- `LocalSecurityFactory` creates local threat detection and risk-scoring services.
- `CloudSecurityFactory` creates cloud-based equivalents.

The `SecurityAnalysisPlatform` depends on the factory abstraction rather than a specific provider.

## Why Abstract Factory?

Abstract Factory was selected because threat detection and risk scoring are related services that may need to change together when the underlying provider changes. The platform can switch between local and cloud service families without modifying its analysis logic.

This reduces coupling between the application and concrete service implementations and supports extensibility. A further provider could be introduced by implementing the same factory and service interfaces.

## Testing

Three unit tests verify that:

- the local factory creates a compatible family of services;
- the cloud factory creates a compatible family of services;
- the provider family can be switched without changing the client.

All three tests pass successfully.

## Critical Reflection

The pattern provides a clear boundary between service creation and service use, which could be valuable in an AI-enabled system where models or external providers may change over time. It also improves testability because alternative implementations can be substituted behind common interfaces.

However, Abstract Factory introduces additional interfaces and classes. If an application only had one fixed provider, this structure could create unnecessary complexity. Adding an entirely new type of service would also require changes across each factory implementation. The pattern is therefore most appropriate when multiple related service families genuinely need to be interchangeable.

This example represents architectural readiness for replaceable AI-oriented services rather than a production AI model or live cloud integration.

## Files

- `unit12_ai_abstract_factory.py` – Abstract Factory implementation.
- `test_unit12_ai_abstract_factory.py` – unit tests for provider-family creation and substitution.
