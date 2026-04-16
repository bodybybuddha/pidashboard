# Dashboard Architecture Overview

This document describes the overall architecture of the custom Raspberry Pi dashboard.

## Goals
- Stream Deck-like layered controls
- Multi-pane layout (control + content)
- Video + data + controls
- Plugin extensibility
- Offline-first capable
- Python-first architecture

## Core Philosophy
This is not a web app — it is a **UI appliance**.

## High-Level Components
- PySide6 (Qt) → UI shell
- FastAPI → backend core
- MQTT → event backbone
- Web UI → rendering layer
- Plugins → extensibility layer

## Layout Concept
- Left pane: controls (layered)
- Right pane: dynamic content
- Layouts can change per mode

