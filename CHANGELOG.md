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
