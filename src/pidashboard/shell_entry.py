from pidashboard.shell.launch import build_launch_plan
from pidashboard.shell.runtime import config_from_env


def main() -> int:
    plan = build_launch_plan(config_from_env())
    # Stage 4/5 contract placeholder: real PySide6 launch wiring lands next.
    if not plan.get("available", False):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
