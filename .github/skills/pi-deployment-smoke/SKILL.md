---
name: pi-deployment-smoke
description: 'Use when validating Raspberry Pi deployment readiness, systemd startup, and kiosk runtime smoke checks.'
---

# Pi Deployment Smoke Skill

## Use When

- Preparing first deployment to Raspberry Pi.
- Verifying service restart safety after updates.
- Troubleshooting startup or kiosk shell runtime issues.

## Inputs

- Deployment scripts and service definitions.
- Runtime environment variables.
- Pi host access and log paths.

## Steps

1. Validate service unit syntax and executable paths.
2. Start or restart services and capture status.
3. Confirm backend health endpoint availability.
4. Confirm kiosk shell launches and points to expected local URL.
5. Capture log excerpts for failed checks and classify root cause area.

## Output

- Smoke checklist with pass or fail per item.
- Service and runtime diagnostics summary.
- Ordered remediation actions.
