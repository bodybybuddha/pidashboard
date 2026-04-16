#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="/opt/pidashboard"
VENV_PATH="${ROOT_DIR}/.venv"

cd "${ROOT_DIR}"
source "${VENV_PATH}/bin/activate"

HOST="${PIDASHBOARD_HOST:-0.0.0.0}"
PORT="${PIDASHBOARD_PORT:-8000}"

exec uvicorn pidashboard.main:app --host "${HOST}" --port "${PORT}"
