# System Architecture

## Components

### 1. PySide6 Shell
- Fullscreen kiosk mode
- Embedded browser (QWebEngineView)

### 2. FastAPI Core
- Serves UI
- Handles state
- WebSocket updates

### 3. MQTT Layer
- Subscribes to device events
- Publishes commands

### 4. Plugin System
- Modular extensions

## Data Flow
Devices → MQTT → FastAPI → WebSocket → UI

UI → FastAPI → MQTT → Devices
