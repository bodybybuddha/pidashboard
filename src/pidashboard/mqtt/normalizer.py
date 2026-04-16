from __future__ import annotations

import json
from typing import Any


def decode_payload(payload_raw: str) -> Any:
    """Decode JSON when possible; otherwise return the original text payload."""
    try:
        return json.loads(payload_raw)
    except json.JSONDecodeError:
        return payload_raw


def normalize_message(topic: str, payload_raw: str) -> dict[str, Any] | None:
    """Map MQTT topic/payload pairs into explicit state mutation intents."""
    payload = decode_payload(payload_raw)

    if topic == "dashboard/mode":
        if isinstance(payload, dict):
            mode = payload.get("mode")
        else:
            mode = payload

        if isinstance(mode, str) and mode.strip():
            return {"kind": "mode", "value": mode.strip()}
        return None

    parts = topic.split("/")
    if len(parts) == 2 and parts[1] == "status":
        device = parts[0]
        if isinstance(payload, str):
            status = payload.strip()
        else:
            status = str(payload)

        if status:
            return {"kind": "device_status", "device": device, "status": status}

    return None
