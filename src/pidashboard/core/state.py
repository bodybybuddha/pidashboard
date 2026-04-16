from __future__ import annotations

from copy import deepcopy
from datetime import UTC, datetime
from typing import Any


class StateStore:
    """In-memory state store used as the single live UI source of truth."""

    def __init__(self) -> None:
        self._state: dict[str, Any] = {
            "mode": "home",
            "devices": {},
            "updated_at": self._now_iso(),
        }

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(UTC).isoformat()

    def snapshot(self) -> dict[str, Any]:
        return deepcopy(self._state)

    def update_mode(self, mode: str) -> dict[str, Any]:
        self._state["mode"] = mode
        self._state["updated_at"] = self._now_iso()
        return self.snapshot()

    def upsert_device_status(self, device: str, status: str) -> dict[str, Any]:
        devices = self._state.setdefault("devices", {})
        devices[device] = {"status": status}
        self._state["updated_at"] = self._now_iso()
        return self.snapshot()
