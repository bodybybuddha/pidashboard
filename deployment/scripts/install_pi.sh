#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="/opt/pidashboard"
INSTALL_SYSTEMD=0
START_SERVICES=0
RUN_SMOKE=0
INSTALL_DEV_DEPS=1

usage() {
  cat <<'EOF'
Usage: install_pi.sh [options]

Options:
  --project-dir <path>   Project root path (default: /opt/pidashboard)
  --with-systemd         Install and enable systemd units
  --start-services       Start systemd services (requires --with-systemd)
  --run-smoke            Run deployment smoke check at the end
  --no-dev               Install package without dev dependencies
  -h, --help             Show this help message

Examples:
  deployment/scripts/install_pi.sh --project-dir "$PWD"
  deployment/scripts/install_pi.sh --project-dir /opt/pidashboard --with-systemd --start-services --run-smoke
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project-dir)
      PROJECT_DIR="$2"
      shift 2
      ;;
    --with-systemd)
      INSTALL_SYSTEMD=1
      shift
      ;;
    --start-services)
      START_SERVICES=1
      shift
      ;;
    --run-smoke)
      RUN_SMOKE=1
      shift
      ;;
    --no-dev)
      INSTALL_DEV_DEPS=0
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ ! -d "$PROJECT_DIR" ]]; then
  echo "Project directory not found: $PROJECT_DIR" >&2
  exit 1
fi

if [[ ! -f "$PROJECT_DIR/pyproject.toml" ]]; then
  echo "pyproject.toml missing in $PROJECT_DIR" >&2
  exit 1
fi

if [[ "$START_SERVICES" -eq 1 && "$INSTALL_SYSTEMD" -eq 0 ]]; then
  echo "--start-services requires --with-systemd" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required" >&2
  exit 1
fi

cd "$PROJECT_DIR"

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi

# shellcheck source=/dev/null
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel >/dev/null

if [[ "$INSTALL_DEV_DEPS" -eq 1 ]]; then
  pip install -e .[dev]
else
  pip install -e .
fi

if [[ ! -f deployment/env/pidashboard.env ]]; then
  cp deployment/env/pidashboard.env.example deployment/env/pidashboard.env
fi

if [[ "$INSTALL_SYSTEMD" -eq 1 ]]; then
  SUDO=""
  if [[ "$(id -u)" -ne 0 ]]; then
    SUDO="sudo"
  fi

  $SUDO cp deployment/systemd/pidashboard-api.service /etc/systemd/system/
  $SUDO cp deployment/systemd/pidashboard-kiosk.service /etc/systemd/system/
  $SUDO systemctl daemon-reload
  $SUDO systemctl enable pidashboard-api.service
  $SUDO systemctl enable pidashboard-kiosk.service

  if [[ "$START_SERVICES" -eq 1 ]]; then
    $SUDO systemctl restart pidashboard-api.service
    $SUDO systemctl restart pidashboard-kiosk.service
  fi
fi

if [[ "$RUN_SMOKE" -eq 1 ]]; then
  PIDASHBOARD_BACKEND_URL="${PIDASHBOARD_BACKEND_URL:-http://127.0.0.1:8000}" \
    deployment/scripts/smoke_check.sh
fi

echo "Installer complete."
echo "Project: $PROJECT_DIR"
echo "Systemd installed: $INSTALL_SYSTEMD"
echo "Services started: $START_SERVICES"
echo "Smoke run: $RUN_SMOKE"
