"""Decision-engine tests: Meridian plus contrast cases."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from fde_scoping.recommend import recommend

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "meridian_health.json"


class MeridianDecisionTests(unittest.TestCase):
    def setUp(self) -> None:
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.facts = payload["facts"]
        self.expected = payload["expected"]

    def test_meridian_is_readiness_then_review(self) -> None:
        rec = recommend(self.facts)
        self.assertEqual(rec.primary, self.expected["primary"])
        self.assertEqual(rec.secondary, self.expected["secondary"])
        self.assertEqual(rec.kpi, self.expected["kpi"])
        self.assertEqual(rec.surface, self.expected["surface"])
        self.assertEqual(set(rec.rejected), set(self.expected["rejected"]))
        self.assertEqual(len(rec.kill_questions), 3)
        self.assertIn("act-on vs dismiss", rec.week3_proof)
        self.assertIn("90-day", rec.board_proof)
        self.assertNotIn("cycle time", rec.week3_proof.lower())

    def test_cloud_agents_are_rejected_on_these_facts(self) -> None:
        rec = recommend(self.facts)
        self.assertIn("Cloud Agents now", rec.rejected)
        self.assertTrue(any("follow-on" in p.lower() or "cloud" in p.lower() for p in rec.pushback))


class ContrastCaseTests(unittest.TestCase):
    def test_used_standard_skips_readiness(self) -> None:
        rec = recommend(
            {
                "shared_config_repo": True,
                "rules_usage_known": True,
                "pr_cycle_days": [4, 5],
                "stated_constraint": "reviewer_availability",
                "budget_weeks": 4,
                "sdk_askers": 0,
                "security_formal": True,
            }
        )
        self.assertEqual(rec.primary, "Cursor Review and Bugbot")
        self.assertIsNone(rec.secondary)
        self.assertIn("Enterprise Readiness", rec.rejected)

    def test_no_numbered_bottleneck_is_readiness_only(self) -> None:
        rec = recommend(
            {
                "shared_config_repo": False,
                "rules_usage_known": False,
                "budget_weeks": 4,
                "adoption_flat_months": 5,
            }
        )
        self.assertEqual(rec.primary, "Enterprise Readiness")
        self.assertIsNone(rec.secondary)
        self.assertIsNone(rec.kpi)
        self.assertIn("Cursor Review and Bugbot", rec.rejected)

    def test_ready_for_cloud_agents(self) -> None:
        rec = recommend(
            {
                "shared_config_repo": True,
                "rules_usage_known": True,
                "security_formal": True,
                "cto_wants": "cloud_agents",
                "review_stage_works": True,
                "write_stage_started": True,
            }
        )
        self.assertEqual(rec.primary, "Cloud Agents")
        self.assertIn("vendor demo", rec.board_proof)

    def test_sdk_not_granted_when_nothing_has_shipped(self) -> None:
        rec = recommend(
            {
                "shared_config_repo": False,
                "sdk_askers": 15,
                "pr_cycle_days": [4, 5],
                "stated_constraint": "reviewer_availability",
                "budget_weeks": 4,
            }
        )
        self.assertIn("SDK now", rec.rejected)
        self.assertTrue(any("SDK" in p for p in rec.pushback))


if __name__ == "__main__":
    unittest.main()
