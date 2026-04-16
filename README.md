# PiDashboard

PiDashboard is a Raspberry Pi-focused dashboard appliance that combines:

- FastAPI backend APIs and WebSocket fan-out
- MQTT ingestion and command routing
- Jinja + HTMX pane/card UI rendering
- PySide6 kiosk shell hosting
- Plugin-based card and route extensions

## Repository Workflow

- All work starts on a dedicated `feature/*` branch.
- Open PR from feature branch to `dev`.
- Open PR from `dev` to `main` after validation.
- Merged feature branches are removed automatically.

## Quick Start

1. Create a virtual environment.
2. Install project dependencies.
3. Run the API scaffold.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn pidashboard.main:app --reload
```

## Project Layout

- `src/pidashboard/core`: state and websocket contracts
- `src/pidashboard/mqtt`: mqtt adapters and payload normalization
- `src/pidashboard/ui`: server-rendered panes/cards
- `src/pidashboard/plugins`: plugin interfaces and registration
- `src/pidashboard/shell`: PySide6 kiosk shell
- `src/pidashboard/deployment`: deployment and runtime assets
- `tests`: unit, integration, and contract tests
- `dashboard_docs`: architecture, wave plans, and progress logs
