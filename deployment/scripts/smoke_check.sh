#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${PIDASHBOARD_BACKEND_URL:-http://127.0.0.1:8000}"

curl -fsS "${BASE_URL}/health" | grep -q '"status":"ok"'
curl -fsS "${BASE_URL}/api/system/shell/launch-plan" >/dev/null
curl -fsS "${BASE_URL}/api/system/deployment/readiness" >/dev/null

echo "smoke-check: pass"
