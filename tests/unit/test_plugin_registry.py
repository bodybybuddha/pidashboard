from pidashboard.plugins.contracts import Card
from pidashboard.plugins.registry import PluginRegistry


class GoodPlugin:
    name = "good"

    def get_cards(self, state: dict) -> list[Card]:
        return [Card(card_id="ok", title="OK", body=state.get("mode", ""))]


class BadPlugin:
    name = "bad"

    def get_cards(self, state: dict) -> list[Card]:
        raise RuntimeError("boom")


def test_registry_isolates_plugin_failures() -> None:
    registry = PluginRegistry()
    registry.register(BadPlugin())
    registry.register(GoodPlugin())

    cards = registry.list_cards({"mode": "focus"})

    assert len(cards) == 1
    assert cards[0].title == "OK"
