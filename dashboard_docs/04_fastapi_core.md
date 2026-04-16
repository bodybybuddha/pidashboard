# FastAPI Core

## Responsibilities
- Serve HTML
- API endpoints
- WebSocket updates
- State management

## Example WebSocket

```python
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        await ws.send_json(state)
```

## Example Route

```python
@app.post("/action/set_mode")
def set_mode(mode: str):
    state["mode"] = mode
```
