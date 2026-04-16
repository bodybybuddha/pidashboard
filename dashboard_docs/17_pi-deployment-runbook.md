# Raspberry Pi Deployment Runbook

## 1. Copy and prepare project

1. Copy project to target path:
   - `/opt/pidashboard`
2. Create venv and install dependencies:
   - `python3 -m venv /opt/pidashboard/.venv`
   - `source /opt/pidashboard/.venv/bin/activate`
   - `pip install -e .[dev]`

## 2. Configure environment

1. Copy template:
   - `cp deployment/env/pidashboard.env.example deployment/env/pidashboard.env`
2. Edit runtime values in deployment/env/pidashboard.env.

## 3. Install systemd units

1. Copy service files:
   - `sudo cp deployment/systemd/pidashboard-api.service /etc/systemd/system/`
   - `sudo cp deployment/systemd/pidashboard-kiosk.service /etc/systemd/system/`
2. Reload and enable:
   - `sudo systemctl daemon-reload`
   - `sudo systemctl enable pidashboard-api.service`
   - `sudo systemctl enable pidashboard-kiosk.service`
3. Start services:
   - `sudo systemctl start pidashboard-api.service`
   - `sudo systemctl start pidashboard-kiosk.service`

## 4. Validate deployment

1. Run smoke checks:
   - `PIDASHBOARD_BACKEND_URL=http://127.0.0.1:8000 deployment/scripts/smoke_check.sh`
2. Inspect service status:
   - `systemctl status pidashboard-api.service --no-pager`
   - `systemctl status pidashboard-kiosk.service --no-pager`
3. Inspect logs:
   - `journalctl -u pidashboard-api.service -n 100 --no-pager`
   - `journalctl -u pidashboard-kiosk.service -n 100 --no-pager`

## 5. Restart safety checks

1. Restart each service and confirm health endpoint:
   - `sudo systemctl restart pidashboard-api.service`
   - `curl -fsS http://127.0.0.1:8000/health`
2. Reboot and re-check status/logs.

## 6. Rollback

1. Disable kiosk service if startup fails:
   - `sudo systemctl disable --now pidashboard-kiosk.service`
2. Keep API service active for diagnostics.
3. Revert to known good commit and redeploy.
