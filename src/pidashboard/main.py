from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

from pidashboard.core.state import StateStore
from pidashboard.core.websocket import WebSocketManager
from pidashboard.mqtt.ingestion import MQTTIngestionService

app = FastAPI(title="PiDashboard", version="0.1.0")
state_store = StateStore()
ws_manager = WebSocketManager()
mqtt_ingestion = MQTTIngestionService(state_store=state_store)


class ModeUpdateRequest(BaseModel):
    mode: str = Field(min_length=1, max_length=64)


class MQTTIngestRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=128)
    payload: str = Field(min_length=1, max_length=4096)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/state", tags=["state"])
def get_state() -> dict:
    return state_store.snapshot()


@app.post("/api/state/mode", tags=["state"])
async def set_mode(payload: ModeUpdateRequest) -> dict:
    snapshot = state_store.update_mode(payload.mode)
    await ws_manager.broadcast_json({"type": "state.update", "state": snapshot})
    return snapshot


@app.post("/api/mqtt/ingest", tags=["mqtt"])
async def ingest_mqtt(payload: MQTTIngestRequest) -> dict:
    snapshot = mqtt_ingestion.ingest(topic=payload.topic, payload_raw=payload.payload)
    if snapshot is not None:
        await ws_manager.broadcast_json({"type": "state.update", "state": snapshot})
        return {"accepted": True, "state": snapshot}

    return {"accepted": False, "reason": "message_not_mapped"}


@app.websocket("/ws")
async def state_updates(websocket: WebSocket) -> None:
    await ws_manager.connect(websocket)
    await websocket.send_json({"type": "state.snapshot", "state": state_store.snapshot()})
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
