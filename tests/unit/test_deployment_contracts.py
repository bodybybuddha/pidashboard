from pidashboard.deployment.contracts import check_deployment_readiness


def test_deployment_readiness_reports_missing_keys() -> None:
    readiness = check_deployment_readiness(env={"PIDASHBOARD_HOST": "0.0.0.0"})

    assert readiness.ready is False
    assert "PIDASHBOARD_PORT" in readiness.missing
    assert "PIDASHBOARD_BACKEND_URL" in readiness.missing


def test_deployment_readiness_true_when_all_keys_present() -> None:
    readiness = check_deployment_readiness(
        env={
            "PIDASHBOARD_HOST": "0.0.0.0",
            "PIDASHBOARD_PORT": "8000",
            "PIDASHBOARD_BACKEND_URL": "http://127.0.0.1:8000",
        }
    )

    assert readiness.ready is True
    assert readiness.missing == []
