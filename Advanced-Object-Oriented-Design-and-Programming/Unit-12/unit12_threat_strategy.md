# Unit 12 – Strategy Pattern: Threat Scoring

## Overview

This artefact demonstrates the Strategy design pattern through a cybersecurity threat-scoring scenario. The `ThreatAnalyzer` delegates the scoring calculation to an interchangeable `ThreatScoringStrategy`.

Two strategies are implemented:

- `StandardThreatStrategy` for general-purpose threat scoring.
- `StrictThreatStrategy` for environments requiring more sensitive scoring.

## Why Strategy?

Strategy was selected because threat-scoring rules may vary according to security requirements, organisational risk appetite or operating context. Keeping each algorithm in a separate strategy avoids embedding multiple scoring rules directly inside `ThreatAnalyzer`.

The analyzer depends on the strategy abstraction, allowing the algorithm to be changed at runtime through `set_strategy()` without changing the client-facing analysis operation.

## Testing

Five unit tests verify:

- standard threat-score calculation;
- the effect of an unusual login location;
- different behaviour between standard and strict strategies;
- runtime replacement of the scoring strategy;
- enforcement of the maximum score of 100.

All five tests pass successfully.

## Critical Reflection

Strategy improves extensibility because another scoring algorithm could be introduced without modifying the existing strategies or the core `ThreatAnalyzer`. Individual algorithms can also be tested independently, reducing the impact of changes to one scoring approach.

The runtime switching demonstrated here is useful where different security contexts require different risk thresholds or scoring policies. However, Strategy introduces additional classes and indirection. If the application had only one stable scoring algorithm, a separate strategy hierarchy would provide little benefit and could amount to overengineering.

The numerical weights used in this demonstration are illustrative rather than empirically validated security-risk values. A production system would require evidence-based thresholds, validation against representative data and appropriate monitoring before such scores were used for security decisions.

## Files

- `unit12_threat_strategy.py` – Strategy pattern implementation.
- `test_unit12_threat_strategy.py` – unit tests covering scoring behaviour and runtime strategy replacement.
