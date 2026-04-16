# Changelog

All notable changes to this project will be documented in this file.

The format follows Keep a Changelog conventions and semantic versioning intent.

## [Unreleased]

### Added
- Initial repository scaffolding for PiDashboard source, tests, and documentation.
- v1 multi-stage plan and progress tracking documents in `dashboard_docs`.
- Root project standards files (`README`, `CONTRIBUTING`, `SECURITY`, `.gitignore`, `pyproject.toml`).
- Core Stage 1 contracts: in-memory state store, websocket manager, state snapshot/update API routes, and websocket state stream endpoint.
- Unit and integration tests for state mutation, API snapshot access, and websocket update fan-out behavior.
- Stage 2 MQTT normalization and ingest slice: topic normalizer, ingestion service, and `/api/mqtt/ingest` contract route.
- Device status state mutations and MQTT-focused unit/integration contract tests.
- Stage 3 UI/plugin slice: plugin contracts and registry, default card plugins, and server-rendered dashboard route with template-backed cards.
- Stage 3 tests covering plugin failure isolation and dashboard HTML card rendering.
- Stage 4 shell/runtime slice: shell runtime config/readiness utilities, launch-plan builder, and `/api/system/shell/launch-plan` contract endpoint.
- Stage 4 tests for readiness timing behavior, launch-plan contracts, and API surface verification.
