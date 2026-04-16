---
description: 'Git workflow policy for feature branches, PR flow to dev/main, and merged branch cleanup.'
applyTo: '**/*'
---

# Git Workflow Policy

## Required Flow

- Create a dedicated `feature/*` branch for every change.
- Open PR from `feature/*` to `dev`.
- After `dev` validation, open PR from `dev` to `main`.

## Branch Rules

- Do not commit directly to `main`.
- Do not commit directly to `dev` unless explicitly approved for emergency fixes.
- Delete feature branches once merged into `dev`.
- Do not keep merged feature branches.

## Operational Guidance

- Keep branch scope narrow to one change set.
- Ensure CI/test checks pass before merge.
- Use descriptive branch names, for example: `feature/mqtt-normalizer`, `feature/ui-pane-layout`.
