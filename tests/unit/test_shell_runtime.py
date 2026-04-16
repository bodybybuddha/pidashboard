from pidashboard.shell.runtime import ShellRuntimeConfig, config_from_env, wait_for_backend_ready


class EventuallyReadyProbe:
    def __init__(self, ready_after: int) -> None:
        self.calls = 0
        self.ready_after = ready_after

    def check(self) -> bool:
        self.calls += 1
        return self.calls >= self.ready_after


def test_wait_for_backend_ready_returns_true_when_probe_eventually_ready() -> None:
    probe = EventuallyReadyProbe(ready_after=3)
    now_values = iter([0.0, 0.1, 0.2, 0.3, 0.4])

    result = wait_for_backend_ready(
        probe=probe,
        timeout_seconds=1,
        poll_interval_seconds=0,
        now=lambda: next(now_values),
        sleep=lambda _: None,
    )

    assert result is True


def test_wait_for_backend_ready_times_out() -> None:
    probe = EventuallyReadyProbe(ready_after=999)
    now_values = iter([0.0, 0.1, 0.2, 0.3, 1.1])

    result = wait_for_backend_ready(
        probe=probe,
        timeout_seconds=1,
        poll_interval_seconds=0,
        now=lambda: next(now_values),
        sleep=lambda _: None,
    )

    assert result is False


def test_config_from_env_defaults(monkeypatch) -> None:
    monkeypatch.delenv("PIDASHBOARD_BACKEND_URL", raising=False)
    monkeypatch.delenv("PIDASHBOARD_KIOSK_FULLSCREEN", raising=False)
    monkeypatch.delenv("PIDASHBOARD_STARTUP_TIMEOUT", raising=False)
    monkeypatch.delenv("PIDASHBOARD_STARTUP_POLL", raising=False)

    config = config_from_env()

    assert isinstance(config, ShellRuntimeConfig)
    assert config.backend_url == "http://127.0.0.1:8000"
    assert config.fullscreen is True
    assert config.startup_timeout_seconds == 15.0
    assert config.poll_interval_seconds == 0.25
