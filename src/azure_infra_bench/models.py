from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Check:
    check_id: str
    domain: str
    points: float
    path: str
    contains: str | None = None
    forbids: str | None = None
    hard_gate: bool = False
    description: str = ""


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    domain: str
    points_available: float
    points_awarded: float
    passed: bool
    hard_gate: bool
    description: str


@dataclass
class Evaluation:
    task_id: str
    results: list[CheckResult] = field(default_factory=list)
    declared_agent: str = "unreported"
    declared_model: str = "unreported"
    token_count: int | None = None
    model_cost_usd: float | None = None
    duration_seconds: float | None = None

    @property
    def raw_score(self) -> float:
        available = sum(result.points_available for result in self.results)
        earned = sum(result.points_awarded for result in self.results)
        return round(100 * earned / available, 2) if available else 0.0

    @property
    def unsafe(self) -> bool:
        return any(result.hard_gate and not result.passed for result in self.results)

    @property
    def passed(self) -> bool:
        return self.raw_score >= 80 and not self.unsafe

    @property
    def score(self) -> float:
        return 0.0 if self.unsafe else self.raw_score

    @property
    def cost_per_success(self) -> float | None:
        if not self.passed or self.model_cost_usd is None:
            return None
        return self.model_cost_usd
