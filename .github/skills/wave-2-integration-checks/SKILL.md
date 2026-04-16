---
name: wave-2-integration-checks
description: 'Use when validating Wave 2 integration between backend contracts, UI rendering, and plugin framework before promotion.'
---

# Wave 2 Integration Checks Skill

## Use When

- Wave 1 is complete and Wave 2 work is in progress.
- Preparing to merge UI and plugin framework lanes.
- Verifying contract compatibility before advancing waves.

## Inputs

- Backend state and WebSocket contract behavior.
- UI pane and card rendering paths.
- Plugin registration and route wiring.

## Steps

1. Confirm state payload shape consumed by UI matches backend output.
2. Validate WebSocket update handling for incremental UI refresh.
3. Verify plugin route and card registration are deterministic.
4. Run focused smoke checks across control, data, and video pane pathways.
5. Report findings by severity and list blockers for wave advancement.

## Output

- Gate decision: pass, pass-with-risks, fail.
- Integration defects with impacted paths.
- Required follow-up tasks.
