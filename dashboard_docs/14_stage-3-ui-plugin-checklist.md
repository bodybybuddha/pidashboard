# Stage 3 UI and Plugin Checklist

## Completed

- [x] Added plugin contract objects for card output
- [x] Added plugin registry with failure isolation
- [x] Added default plugins for mode/device cards
- [x] Added server-rendered dashboard route (`GET /`)
- [x] Added dashboard template for pane/card layout
- [x] Added Stage 3 unit and integration tests

## Validation

- [x] `pytest -q` passes with Stage 3 additions (`14 passed`)

## Remaining for Stage 3 Exit

- [ ] Add HTMX partial update endpoints for pane/card refreshes
- [ ] Integrate websocket-driven card update hooks in rendered templates
- [ ] Expand plugin discovery beyond default in-process registration
