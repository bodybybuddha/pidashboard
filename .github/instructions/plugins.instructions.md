---
description: 'Plugin development rules for stable interfaces, registration safety, and predictable lifecycle.'
applyTo: '**/plugins/**/*.py'
---

# Plugin Rules

- Implement required plugin interface methods consistently.
- Register cards and routes through the framework only.
- Fail a single plugin safely without crashing global startup.
- Keep plugin configuration explicit and documented.
