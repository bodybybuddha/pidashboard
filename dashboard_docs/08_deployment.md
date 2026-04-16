# Deployment

## On Raspberry Pi

1. Install dependencies
2. Run FastAPI
3. Launch PySide6 app

## Systemd Service

```ini
[Service]
ExecStart=python main.py
Restart=always
```

## Kiosk Mode
- Fullscreen Qt
- No OS chrome
