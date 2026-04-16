from pidashboard.mqtt.normalizer import normalize_message


def test_normalize_dashboard_mode_plain_payload() -> None:
    normalized = normalize_message("dashboard/mode", "focus")
    assert normalized == {"kind": "mode", "value": "focus"}


def test_normalize_dashboard_mode_json_payload() -> None:
    normalized = normalize_message("dashboard/mode", '{"mode":"media"}')
    assert normalized == {"kind": "mode", "value": "media"}


def test_normalize_device_status_payload() -> None:
    normalized = normalize_message("printer/status", "ready")
    assert normalized == {
        "kind": "device_status",
        "device": "printer",
        "status": "ready",
    }


def test_normalize_unmapped_topic_returns_none() -> None:
    assert normalize_message("printer/unknown", "ready") is None
