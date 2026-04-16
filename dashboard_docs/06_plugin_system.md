# Plugin System

## Goals
- Extend functionality
- Add new cards/panes
- Integrate services

## Plugin Structure

```python
class Plugin:
    def get_cards(self): pass
    def get_routes(self): pass
```

## Example Plugins
- Weather
- Stocks
- Bambu printer
- Cameras
- YouTube
