from fastapi.testclient import TestClient

from pidashboard.main import app


def test_dashboard_route_renders_plugin_cards() -> None:
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    html = response.text
    assert "Current Mode" in html
    assert "Connected Devices" in html
