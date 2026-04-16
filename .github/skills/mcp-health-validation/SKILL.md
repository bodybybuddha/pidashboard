---
name: mcp-health-validation
description: 'Use when validating MCP server readiness, auth wiring, and workspace mcp configuration before implementation or testing.'
---

# MCP Health Validation Skill

## Use When

- User asks to verify MCP setup.
- MCP tools fail unexpectedly.
- Before starting a new implementation wave.

## Inputs

- Workspace MCP config file.
- Environment variable availability.
- Installed MCP package inventory.

## Steps

1. Validate JSON syntax for workspace MCP configuration.
2. Verify expected MCP packages are installed and discoverable.
3. Check required environment variables for configured servers.
4. Produce a per-server readiness report with status: ready, partial, blocked.
5. Suggest exact remediation commands for any blocked servers.

## Output

- MCP readiness matrix by server.
- Missing env vars and install gaps.
- Recommended next action order.
