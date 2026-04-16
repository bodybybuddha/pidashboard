#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="/opt/pidashboard"
VENV_PATH="${ROOT_DIR}/.venv"

cd "${ROOT_DIR}"
source "${VENV_PATH}/bin/activate"

python -m pidashboard.shell_entry
