# AGENTS.md

## Project Overview

PiDashboard is a Raspberry Pi-focused dashboard appliance that combines:
- FastAPI for backend APIs and WebSocket state fan-out
- MQTT for event ingestion and device command routing
- Jinja + HTMX for server-rendered UI panes and cards
- PySide6 shell for kiosk fullscreen hosting
- Plugin-based extensions for cards, routes, and integrations

Primary design docs live in dashboard_docs.

## Architecture Contracts

Implement against these contracts before broad feature work:
- State store is the single source of truth for live UI
- MQTT payloads are normalized before entering state
- UI receives incremental updates through WebSocket broadcasts
- Plugins provide cards and routes through a stable plugin interface

## Working Conventions

- Keep module boundaries strict: core, mqtt, ui, plugins, shell, deployment.
- Prefer additive changes over rewrites.
- Add tests for state flow and integration touchpoints.
- Never hardcode secrets or broker credentials.

## Suggested Build Waves

1. Wave 1: FastAPI core + state + WebSocket + MQTT skeleton
2. Wave 2: UI rendering + plugin framework + PySide shell in parallel
3. Wave 3: Default plugins, integration tests, deployment hardening

## Definition of Done

- Core flow validated: MQTT event -> state update -> WebSocket push -> UI change
- Smoke tests pass for API and WebSocket paths
- Plugin loading and route registration are deterministic
- Raspberry Pi service startup and restart behavior documented

## Safety and Quality

- Keep dependencies minimal and pinned where practical.
- Validate new paths with lint and tests before declaring completion.
- Preserve existing docs intent in dashboard_docs unless explicitly updated.
