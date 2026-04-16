from pidashboard.core.state import StateStore


def test_state_store_snapshot_is_defensive_copy() -> None:
    store = StateStore()
    snapshot = store.snapshot()
    snapshot["mode"] = "mutated"

    assert store.snapshot()["mode"] == "home"


def test_state_store_update_mode_mutates_mode_and_timestamp() -> None:
    store = StateStore()
    before = store.snapshot()["updated_at"]

    updated = store.update_mode("media")

    assert updated["mode"] == "media"
    assert updated["updated_at"] != before
