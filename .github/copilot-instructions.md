# Copilot Instructions

This repository is built in orchestrated waves.

## Default Behavior

- Read dashboard_docs before proposing architecture changes.
- Treat state, MQTT normalization, and WebSocket contracts as first-class.
- Prefer small, testable increments with visible acceptance criteria.

## Coding Priorities

- Backend: reliability and explicit contracts over convenience.
- UI: composable panes and cards over one-off templates.
- Plugins: stable interfaces and predictable registration.
- Deployment: restart safety and clear operational defaults.

## Review Gate

Before wave completion:
- Run tests relevant to edited components.
- Check for obvious integration regressions.
- Document any deferred risk and follow-up task.
