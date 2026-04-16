from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Callable, Protocol
from urllib.request import urlopen


class HealthProbe(Protocol):
    def check(self) -> bool:
        ...


@dataclass(frozen=True)
class ShellRuntimeConfig:
    backend_url: str
    fullscreen: bool
    startup_timeout_seconds: float
    poll_interval_seconds: float


class HTTPHealthProbe:
    """Checks backend /health endpoint for shell startup readiness."""

    def __init__(self, backend_url: str) -> None:
        self._url = backend_url.rstrip("/") + "/health"

    def check(self) -> bool:
        try:
            with urlopen(self._url, timeout=2) as response:  # noqa: S310
                if response.status != 200:
                    return False
                payload = json.loads(response.read().decode("utf-8"))
                return payload.get("status") == "ok"
        except Exception:
            return False


def config_from_env() -> ShellRuntimeConfig:
    return ShellRuntimeConfig(
        backend_url=os.getenv("PIDASHBOARD_BACKEND_URL", "http://127.0.0.1:8000"),
        fullscreen=os.getenv("PIDASHBOARD_KIOSK_FULLSCREEN", "1") == "1",
        startup_timeout_seconds=float(os.getenv("PIDASHBOARD_STARTUP_TIMEOUT", "15")),
        poll_interval_seconds=float(os.getenv("PIDASHBOARD_STARTUP_POLL", "0.25")),
    )


def wait_for_backend_ready(
    probe: HealthProbe,
    timeout_seconds: float,
    poll_interval_seconds: float,
    *,
    now: Callable[[], float] = time.monotonic,
    sleep: Callable[[float], None] = time.sleep,
) -> bool:
    deadline = now() + timeout_seconds
    while now() < deadline:
        if probe.check():
            return True
        sleep(poll_interval_seconds)
    return False
