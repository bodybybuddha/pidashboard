from fastapi.testclient import TestClient

from pidashboard.main import app


def test_mqtt_ingest_mode_updates_state_and_broadcasts() -> None:
    client = TestClient(app)

    with client.websocket_connect("/ws") as websocket:
        initial = websocket.receive_json()
        assert initial["type"] == "state.snapshot"

        response = client.post(
            "/api/mqtt/ingest",
            json={"topic": "dashboard/mode", "payload": '{"mode":"focus"}'},
        )

        assert response.status_code == 200
        body = response.json()
        assert body["accepted"] is True
        assert body["state"]["mode"] == "focus"

        update = websocket.receive_json()
        assert update["type"] == "state.update"
        assert update["state"]["mode"] == "focus"


def test_mqtt_ingest_device_status_updates_state() -> None:
    client = TestClient(app)

    response = client.post(
        "/api/mqtt/ingest",
        json={"topic": "printer/status", "payload": "ready"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["accepted"] is True
    assert body["state"]["devices"]["printer"]["status"] == "ready"


def test_mqtt_ingest_unmapped_message_rejected() -> None:
    client = TestClient(app)

    response = client.post(
        "/api/mqtt/ingest",
        json={"topic": "camera/heartbeat", "payload": "ok"},
    )

    assert response.status_code == 200
    assert response.json() == {"accepted": False, "reason": "message_not_mapped"}
