---
description: 'Backend guidance for FastAPI, state flow, and WebSocket contract safety in PiDashboard.'
applyTo: '**/*.py'
---

# Backend Rules

- Keep request handlers thin and route through service or state layers.
- State updates must be explicit and testable.
- WebSocket broadcasting failures must be contained and logged.
- Normalize device or MQTT payloads before state mutation.

# Testing

- Add tests for contract changes.
- Prefer deterministic fixtures over live broker dependencies in unit tests.
