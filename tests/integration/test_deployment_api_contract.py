from fastapi.testclient import TestClient

from pidashboard.main import app


def test_deployment_readiness_endpoint_contract() -> None:
    client = TestClient(app)

    response = client.get("/api/system/deployment/readiness")

    assert response.status_code == 200
    payload = response.json()
    assert "ready" in payload
    assert "missing" in payload
    assert isinstance(payload["missing"], list)
