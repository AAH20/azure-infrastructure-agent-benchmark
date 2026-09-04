#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m azure_infra_bench.cli list --tasks tasks
python3 scripts/run-suite.py >/dev/null
python3 -m json.tool evidence/reference-results.json >/dev/null
