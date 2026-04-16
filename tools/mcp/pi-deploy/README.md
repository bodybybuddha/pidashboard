# pi-deploy MCP (Scaffold)

Purpose:
- Deploy dashboard service updates to Raspberry Pi.
- Restart and verify systemd services.
- Capture logs and runtime diagnostics.

Next implementation steps:
1. Create MCP server entrypoint.
2. Add tools: deploy_release, restart_service, service_status, tail_logs.
3. Add safe rollout and rollback checks.
