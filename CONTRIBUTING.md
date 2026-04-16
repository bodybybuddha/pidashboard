# Contributing

## Branching

- Create a dedicated `feature/*` branch for each change.
- Open pull requests to `dev` first.
- Promote from `dev` to `main` through a pull request.
- Remove feature branches after merge.

## Development Process

1. Sync with latest `dev`.
2. Implement one focused change set.
3. Add or update tests.
4. Run relevant checks locally.
5. Open PR with a concise change summary and validation notes.

## Commit Style

Use clear, scoped commit messages. Example:

- `feat(mqtt): add topic normalization pipeline`
- `fix(ui): prevent stale card websocket updates`
- `docs(plan): update wave progress`
