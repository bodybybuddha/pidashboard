# Stage 1 Core Contracts Checklist

## Completed

- [x] Implemented in-memory state store contract
- [x] Added explicit state mutation API (`mode`)
- [x] Implemented websocket manager with failure containment
- [x] Added websocket endpoint with initial snapshot + update stream
- [x] Added API endpoint for current state snapshot
- [x] Added unit and integration tests for contract behavior

## Validation

- [x] `pytest -q` passes with Stage 1 tests
- [x] Gate 1 criteria met: API and state contracts are implemented and testable

## Notes

- Broadcast failures are contained by pruning stale websocket connections.
- MQTT normalization is deferred to Stage 2.
