from __future__ import annotations

import logging
from typing import Any

from pidashboard.plugins.contracts import Card, DashboardPlugin

logger = logging.getLogger(__name__)


class PluginRegistry:
    """Registers plugins and renders cards while isolating plugin failures."""

    def __init__(self) -> None:
        self._plugins: list[DashboardPlugin] = []

    def register(self, plugin: DashboardPlugin) -> None:
        self._plugins.append(plugin)

    def list_cards(self, state: dict[str, Any]) -> list[Card]:
        cards: list[Card] = []
        for plugin in self._plugins:
            try:
                cards.extend(plugin.get_cards(state))
            except Exception as exc:
                logger.warning("plugin_failed name=%s error=%s", plugin.name, exc)
        return cards
