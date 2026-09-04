from __future__ import annotations

import json
from pathlib import Path

from .models import Check


def load_task(task_dir: Path) -> tuple[dict, list[Check]]:
    manifest = json.loads((task_dir / "task.json").read_text())
    checks = [Check(**item) for item in manifest["checks"]]
    return manifest, checks


def load_run_metadata(submission_dir: Path) -> dict:
    path = submission_dir / "run.json"
    return json.loads(path.read_text()) if path.exists() else {}
