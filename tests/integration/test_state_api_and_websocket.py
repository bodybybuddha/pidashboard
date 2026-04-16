from fastapi.testclient import TestClient

from pidashboard.main import app


def test_get_state_returns_state_snapshot() -> None:
    client = TestClient(app)
    response = client.get("/api/state")

    assert response.status_code == 200
    payload = response.json()
    assert payload["mode"]
    assert payload["updated_at"]


def test_post_mode_broadcasts_websocket_update() -> None:
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        first_message = websocket.receive_json()
        assert first_message["type"] == "state.snapshot"

        response = client.post("/api/state/mode", json={"mode": "focus"})
        assert response.status_code == 200
        assert response.json()["mode"] == "focus"

        update_message = websocket.receive_json()
        assert update_message["type"] == "state.update"
        assert update_message["state"]["mode"] == "focus"
