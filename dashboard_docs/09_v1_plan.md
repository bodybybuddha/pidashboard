# v1 Multi-Stage Plan

This document defines the staged execution plan to reach PiDashboard v1.

## Scope

v1 success criteria:

- Reliable flow: MQTT event -> state mutation -> WebSocket push -> UI update
- Deterministic plugin loading for cards/routes
- Stable kiosk shell behavior on Raspberry Pi
- Repeatable deployment and restart-safe runtime

## Stage 0: Foundation Scaffolding

Objective:
- Establish repository structure, packaging, baseline docs, and quality entrypoints.

Deliverables:
- Source package layout by domain (`core`, `mqtt`, `ui`, `plugins`, `shell`, `deployment`)
- Test suite layout (`unit`, `integration`, `contracts`)
- Root standards (`README`, `CHANGELOG`, `CONTRIBUTING`, `SECURITY`, `.gitignore`, `pyproject.toml`)
- Initial FastAPI app + `/health` endpoint

Exit Criteria:
- Editable install works
- Basic smoke test passes

## Stage 1: Core Contracts (Gate 1)

Objective:
- Build FastAPI core, central state store, and websocket manager with explicit contracts.

Deliverables:
- State model and mutation API
- WebSocket connection manager and broadcast API
- API routes for state snapshots and control actions
- Contract tests for state + websocket interactions

Exit Criteria:
- API and state contracts implemented and testable
- WebSocket broadcast failures are contained/logged

## Stage 2: MQTT Ingestion + Normalization

Objective:
- Ingest device events via MQTT and normalize payloads before state mutation.

Deliverables:
- MQTT client lifecycle manager
- Topic mapping and payload normalization layer
- Integration path from normalized events into state store
- Deterministic fixtures for contract tests

Exit Criteria:
- MQTT events safely update state through normalization
- Core flow visible in integration tests

## Stage 3: UI Rendering + Plugin Framework (Gate 2)

Objective:
- Render panes/cards with Jinja + HTMX and register plugin-provided content.

Deliverables:
- Base layout templates and pane composition primitives
- Card rendering contracts for plugin output
- Plugin discovery, registration, and failure isolation
- WebSocket-driven incremental UI updates

Exit Criteria:
- UI and plugin framework integrate cleanly with core contracts
- Plugin failure does not crash app startup

## Stage 4: Kiosk Shell + Runtime Integration

Objective:
- Host dashboard in PySide6 shell for fullscreen appliance experience.

Deliverables:
- Shell startup lifecycle and backend readiness checks
- Embedded browser + kiosk mode behavior
- Graceful restart and recovery behavior

Exit Criteria:
- Shell reliably starts and reconnects to backend
- Kiosk UX is stable on target Pi hardware

## Stage 5: Deployment + Hardening (Gate 3)

Objective:
- Prepare production-ready Raspberry Pi deployment and operations.

Deliverables:
- systemd service units and environment handling
- Startup/restart runbook and smoke checks
- Security and dependency review

Exit Criteria:
- Deployment and runtime checks pass for Raspberry Pi usage
- v1 release checklist complete

## Governance

- Branch flow: `feature/*` -> PR -> `dev` -> PR -> `main`
- One focused change set per feature branch
- Remove feature branches after successful merge into `dev`
- Track stage progress in `dashboard_docs/10_progress.md`
