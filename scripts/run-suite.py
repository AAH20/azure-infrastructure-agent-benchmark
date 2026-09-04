#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "src"))

from azure_infra_bench.suite import evaluate_references  # noqa: E402

result = evaluate_references(ROOT / "tasks")
rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
(ROOT / "evidence/reference-results.json").write_text(rendered)
print(rendered, end="")
raise SystemExit(0 if result["passed"] else 1)
