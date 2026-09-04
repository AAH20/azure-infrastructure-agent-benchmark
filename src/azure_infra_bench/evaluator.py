from __future__ import annotations

import re
from pathlib import Path

from .loader import load_run_metadata, load_task
from .models import CheckResult, Evaluation


def _matches(text: str, pattern: str | None) -> bool:
    flags = re.IGNORECASE | re.MULTILINE | re.DOTALL
    return True if pattern is None else re.search(pattern, text, flags) is not None


def evaluate(task_dir: Path, submission_dir: Path) -> Evaluation:
    manifest, checks = load_task(task_dir)
    metadata = load_run_metadata(submission_dir)
    evaluation = Evaluation(
        task_id=manifest["id"],
        declared_agent=metadata.get("agent", "unreported"),
        declared_model=metadata.get("model", "unreported"),
        token_count=metadata.get("token_count"),
        model_cost_usd=metadata.get("model_cost_usd"),
        duration_seconds=metadata.get("duration_seconds"),
    )
    for check in checks:
        target = submission_dir / check.path
        text = target.read_text(encoding="utf-8") if target.is_file() else ""
        passed = target.is_file() and _matches(text, check.contains)
        if check.forbids is not None and _matches(text, check.forbids):
            passed = False
        evaluation.results.append(CheckResult(
            check_id=check.check_id,
            domain=check.domain,
            points_available=check.points,
            points_awarded=check.points if passed else 0.0,
            passed=passed,
            hard_gate=check.hard_gate,
            description=check.description,
        ))
    return evaluation
