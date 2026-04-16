# Deployment

## On Raspberry Pi

1. Install dependencies and create virtual environment.
2. Configure deployment environment file.
3. Install and enable systemd units.
4. Run smoke checks and verify restart behavior.

## Systemd Service

```ini
[Service]
EnvironmentFile=/opt/pidashboard/deployment/env/pidashboard.env
ExecStart=/opt/pidashboard/deployment/scripts/start_api.sh
Restart=always
```

Companion kiosk service:

```ini
[Service]
EnvironmentFile=/opt/pidashboard/deployment/env/pidashboard.env
ExecStart=/opt/pidashboard/deployment/scripts/start_kiosk.sh
Restart=always
```

## Kiosk Mode
- Fullscreen Qt
- No OS chrome

## Smoke Checks

- Verify health endpoint: `/health`
- Verify shell launch plan endpoint: `/api/system/shell/launch-plan`
- Verify deployment readiness endpoint: `/api/system/deployment/readiness`
