from __future__ import annotations

from pathlib import Path

from .evaluator import evaluate
from .reporters import as_dict


def evaluate_references(tasks_root: Path) -> dict:
    rows = []
    for task_file in sorted(tasks_root.glob("*/task.json")):
        task_dir = task_file.parent
        for kind in ("gold", "unsafe"):
            result = evaluate(task_dir, task_dir / "submissions" / kind)
            rows.append({"submission": kind, **as_dict(result)})
    expected = all(row["score"] == 100 for row in rows if row["submission"] == "gold") and all(
        not row["passed"] for row in rows if row["submission"] == "unsafe"
    )
    return {
        "schema_version": "1.0",
        "benchmark_version": "2026.09-mvp",
        "passed": expected,
        "task_count": len(rows) // 2,
        "evaluations": rows,
        "evidence_boundary": "Reference fixture results, not comparative frontier-model measurements.",
    }
