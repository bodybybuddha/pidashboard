from pidashboard.shell.launch import build_launch_plan
from pidashboard.shell.runtime import ShellRuntimeConfig


def test_build_launch_plan_reflects_runtime_config() -> None:
    config = ShellRuntimeConfig(
        backend_url="http://localhost:8000",
        fullscreen=False,
        startup_timeout_seconds=10,
        poll_interval_seconds=0.5,
    )

    plan = build_launch_plan(config)

    assert plan["backend_url"] == "http://localhost:8000"
    assert plan["fullscreen"] is False
    assert "PySide6" in plan["requires"]
    assert "available" in plan
