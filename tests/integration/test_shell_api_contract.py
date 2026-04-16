from fastapi.testclient import TestClient

from pidashboard.main import app


def test_shell_launch_plan_endpoint_returns_contract() -> None:
    client = TestClient(app)

    response = client.get("/api/system/shell/launch-plan")

    assert response.status_code == 200
    payload = response.json()
    assert payload["backend_url"]
    assert isinstance(payload["fullscreen"], bool)
    assert "PySide6" in payload["requires"]
    assert "available" in payload
