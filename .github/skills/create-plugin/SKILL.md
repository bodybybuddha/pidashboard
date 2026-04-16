---
name: create-plugin
description: 'Use when adding a new dashboard plugin that provides cards, optional routes, and integration glue.'
---

# Create Plugin Skill

## Use When

- User asks to add a new data, video, or control plugin.

## Required Contract

- Implement plugin class with card and route registration methods.
- Provide metadata and default configuration.

## Steps

1. Scaffold plugin module and config model.
2. Implement contract methods.
3. Add template snippets and route handlers if needed.
4. Register plugin through framework loader.
5. Add plugin-focused tests.
