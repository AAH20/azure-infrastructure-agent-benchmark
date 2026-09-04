from __future__ import annotations

import argparse
from pathlib import Path

from .evaluator import evaluate
from .reporters import as_json, as_markdown


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate infrastructure-agent submissions.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--tasks", default="tasks")
    eval_parser = subparsers.add_parser("evaluate")
    eval_parser.add_argument("task")
    eval_parser.add_argument("submission")
    eval_parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    eval_parser.add_argument("--output", type=Path)
    eval_parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()

    if args.command == "list":
        for manifest in sorted(Path(args.tasks).glob("*/task.json")):
            print(manifest.parent.name)
        return

    result = evaluate(Path(args.task), Path(args.submission))
    rendered = as_json(result) if args.format == "json" else as_markdown(result)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")
    if args.fail_on_error and not result.passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
