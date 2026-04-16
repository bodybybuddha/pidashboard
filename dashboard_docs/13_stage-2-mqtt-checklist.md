# Stage 2 MQTT Ingestion Checklist

## Completed

- [x] Implemented topic and payload normalization contract
- [x] Added ingestion service that applies explicit state mutations
- [x] Added HTTP ingest contract route for deterministic testability
- [x] Added tests for mode and device status topic mappings
- [x] Added tests for unmapped topic behavior

## Validation

- [x] `pytest -q` passes with Stage 2 additions (`12 passed`)

## Remaining for Stage 2 Exit

- [ ] Add MQTT client lifecycle manager (connect/reconnect/subscribe)
- [ ] Add configurable topic subscription map
- [ ] Add malformed payload and reconnection behavior fixture tests
- [ ] Validate normalized MQTT event -> state update -> websocket push in integration path
