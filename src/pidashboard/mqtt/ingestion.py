from __future__ import annotations

from typing import Any

from pidashboard.core.state import StateStore
from pidashboard.mqtt.normalizer import normalize_message


class MQTTIngestionService:
    """Normalizes MQTT payloads and applies safe, explicit state mutations."""

    def __init__(self, state_store: StateStore) -> None:
        self._state_store = state_store

    def ingest(self, topic: str, payload_raw: str) -> dict[str, Any] | None:
        normalized = normalize_message(topic=topic, payload_raw=payload_raw)
        if normalized is None:
            return None

        if normalized["kind"] == "mode":
            return self._state_store.update_mode(normalized["value"])

        if normalized["kind"] == "device_status":
            return self._state_store.upsert_device_status(
                device=normalized["device"],
                status=normalized["status"],
            )

        return None
