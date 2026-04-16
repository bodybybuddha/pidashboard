from __future__ import annotations

from pidashboard.plugins.contracts import Card


class ModeCardPlugin:
    name = "mode-card"

    def get_cards(self, state: dict) -> list[Card]:
        mode = state.get("mode", "unknown")
        return [Card(card_id="mode", title="Current Mode", body=str(mode))]


class DeviceSummaryPlugin:
    name = "device-summary"

    def get_cards(self, state: dict) -> list[Card]:
        devices = state.get("devices", {})
        total = len(devices)
        return [Card(card_id="devices", title="Connected Devices", body=str(total))]
