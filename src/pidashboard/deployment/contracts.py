from __future__ import annotations

import os
from dataclasses import dataclass

REQUIRED_ENV_KEYS = [
    "PIDASHBOARD_HOST",
    "PIDASHBOARD_PORT",
    "PIDASHBOARD_BACKEND_URL",
]


@dataclass(frozen=True)
class DeploymentReadiness:
    ready: bool
    missing: list[str]


def check_deployment_readiness(env: dict[str, str] | None = None) -> DeploymentReadiness:
    values = env if env is not None else os.environ
    missing = [key for key in REQUIRED_ENV_KEYS if not values.get(key)]
    return DeploymentReadiness(ready=not missing, missing=missing)
