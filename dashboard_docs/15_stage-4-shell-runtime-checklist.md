# Stage 4 Shell Runtime Checklist

## Completed

- [x] Added shell runtime configuration contract
- [x] Added backend readiness polling contract
- [x] Added shell launch-plan builder utility
- [x] Added shell launch-plan API contract route
- [x] Added Stage 4 unit and integration tests

## Validation

- [x] `pytest -q` passes with Stage 4 additions (`19 passed`)

## Remaining for Stage 4 Exit

- [ ] Integrate real PySide6 QWebEngine shell process lifecycle
- [ ] Add restart/reconnect strategy validation on Pi target
- [ ] Add shell startup logs and operational diagnostics
