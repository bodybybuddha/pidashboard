---
name: mqtt-contract-testing
description: 'Use when validating MQTT topic fixtures, normalization rules, and state-to-websocket contract behavior.'
---

# MQTT Contract Testing Skill

## Use When

- Adding or changing MQTT topic handlers.
- Testing normalization logic before UI integration.
- Reproducing event-flow regressions.

## Inputs

- Topic fixtures and payload samples.
- Backend normalization and state update paths.
- WebSocket broadcast behavior.

## Steps

1. Replay representative topic fixtures.
2. Validate normalization outputs against expected schema.
3. Verify state mutation behavior and idempotency expectations.
4. Verify downstream WebSocket payload consistency.
5. Generate a contract test report with mismatches and likely causes.

## Output

- Topic-by-topic contract validation report.
- Failed fixture details with expected vs actual.
- Recommended fixes by component boundary.
