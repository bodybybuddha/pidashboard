from __future__ import annotations

import importlib.util

from pidashboard.shell.runtime import ShellRuntimeConfig


def pyside6_available() -> bool:
    return importlib.util.find_spec("PySide6") is not None


def build_launch_plan(config: ShellRuntimeConfig) -> dict[str, object]:
    """Build a deterministic launch plan for kiosk shell startup scripts."""
    return {
        "backend_url": config.backend_url,
        "fullscreen": config.fullscreen,
        "requires": ["PySide6", "QtWebEngine"],
        "available": pyside6_available(),
    }
