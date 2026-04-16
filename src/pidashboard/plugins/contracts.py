from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class Card:
    card_id: str
    title: str
    body: str


class DashboardPlugin(Protocol):
    name: str

    def get_cards(self, state: dict[str, Any]) -> list[Card]:
        ...
