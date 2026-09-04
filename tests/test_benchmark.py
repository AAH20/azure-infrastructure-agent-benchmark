import json
import tempfile
import unittest
from pathlib import Path

from azure_infra_bench.evaluator import evaluate
from azure_infra_bench.reporters import as_json
from azure_infra_bench.suite import evaluate_references


ROOT = Path(__file__).parents[1]


class BenchmarkTests(unittest.TestCase):
    def test_all_gold_references_pass_and_unsafe_fail(self):
        result = evaluate_references(ROOT / "tasks")
        self.assertTrue(result["passed"])
        self.assertEqual(result["task_count"], 3)
        self.assertTrue(all(
            row["score"] == 100
            for row in result["evaluations"]
            if row["submission"] == "gold"
        ))

    def test_private_dns_unsafe_hits_hard_gate(self):
        task = ROOT / "tasks/private-dns-repair"
        result = evaluate(task, task / "submissions/unsafe")
        self.assertTrue(result.unsafe)
        self.assertEqual(result.score, 0)

    def test_gold_run_economics_are_reported(self):
        task = ROOT / "tasks/private-dns-repair"
        result = json.loads(as_json(evaluate(task, task / "submissions/gold")))
        self.assertEqual(result["agent"], "reference-human")
        self.assertEqual(result["cost_per_success_usd"], 0)

    def test_missing_submission_files_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            result = evaluate(ROOT / "tasks/aks-production-resilience", Path(directory))
            self.assertFalse(result.passed)
            self.assertEqual(result.raw_score, 0)

    def test_score_requires_eighty_percent(self):
        task = ROOT / "tasks/logging-retention-finops"
        result = evaluate(task, task / "submissions/gold")
        self.assertEqual(result.score, 100)
        self.assertTrue(result.passed)


if __name__ == "__main__":
    unittest.main()
