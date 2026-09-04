from __future__ import annotations

import json
from dataclasses import asdict

from .models import Evaluation


def as_dict(evaluation: Evaluation) -> dict:
    domains: dict[str, dict[str, float]] = {}
    for result in evaluation.results:
        bucket = domains.setdefault(result.domain, {"earned": 0.0, "available": 0.0})
        bucket["earned"] += result.points_awarded
        bucket["available"] += result.points_available
    for bucket in domains.values():
        bucket["percent"] = round(100 * bucket["earned"] / bucket["available"], 2)
    return {
        "schema_version": "1.0",
        "task_id": evaluation.task_id,
        "passed": evaluation.passed,
        "unsafe": evaluation.unsafe,
        "score": evaluation.score,
        "raw_score": evaluation.raw_score,
        "agent": evaluation.declared_agent,
        "model": evaluation.declared_model,
        "token_count": evaluation.token_count,
        "model_cost_usd": evaluation.model_cost_usd,
        "cost_per_success_usd": evaluation.cost_per_success,
        "duration_seconds": evaluation.duration_seconds,
        "domains": domains,
        "checks": [asdict(result) for result in evaluation.results],
        "evidence_boundary": "Deterministic fixture evaluation; declared run economics are not independently metered.",
    }


def as_json(evaluation: Evaluation) -> str:
    return json.dumps(as_dict(evaluation), indent=2, sort_keys=True) + "\n"


def as_markdown(evaluation: Evaluation) -> str:
    report = as_dict(evaluation)
    lines = [
        f"# AzureInfraBench: {evaluation.task_id}", "",
        f"**Result:** {'PASS' if evaluation.passed else 'FAIL'}",
        f"**Score:** {evaluation.score:.2f}",
        f"**Unsafe:** {'yes' if evaluation.unsafe else 'no'}", "",
        "| Check | Domain | Result | Points |", "|---|---|---:|---:|",
    ]
    for check in evaluation.results:
        lines.append(
            f"| {check.check_id} | {check.domain} | {'pass' if check.passed else 'fail'} | "
            f"{check.points_awarded:g}/{check.points_available:g} |"
        )
    lines.extend(["", f"> {report['evidence_boundary']}"])
    return "\n".join(lines) + "\n"
