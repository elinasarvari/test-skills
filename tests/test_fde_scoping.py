"""Structural tests for the FDE scoping agent and Meridian memo."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".cursor" / "skills" / "fde-scoping" / "SKILL.md"
ENGAGEMENTS = ROOT / ".cursor" / "skills" / "fde-scoping" / "references" / "engagements.md"
FRAMEWORK = ROOT / ".cursor" / "skills" / "fde-scoping" / "references" / "decision-framework.md"
WORKED = ROOT / ".cursor" / "skills" / "fde-scoping" / "references" / "meridian-health.md"
MEMO = ROOT / "memos" / "meridian-health.md"
AGENT = ROOT / ".cursor" / "agents" / "fde-scoper.md"
FIXTURE = ROOT / "tests" / "fixtures" / "meridian_health.json"

REQUIRED_ENGAGEMENTS = [
    "Enterprise Readiness",
    "Cursor Review and Bugbot",
    "Cloud Agents",
    "SDK",
    "AI SDLC Integration",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class SkillPackageTests(unittest.TestCase):
    def test_skill_frontmatter_and_sections(self) -> None:
        text = _read(SKILL)
        self.assertIn("name: fde-scoping", text)
        self.assertIn("## Memo shape (required)", text)
        for heading in (
            "Recommendation and alternatives",
            "Pushback",
            "Three discovery questions",
            "Week-3 checkpoint vs board update",
            "Bear case",
        ):
            self.assertIn(heading, text)
        self.assertIn("four weeks will not move", text.lower())
        self.assertIn("do not promise a percentage", text.lower())
        self.assertIn("Align on the problem", text)

    def test_catalog_names_every_sellable_engagement(self) -> None:
        text = _read(ENGAGEMENTS)
        for name in REQUIRED_ENGAGEMENTS:
            self.assertIn(name, text)
        self.assertIn("Causal mechanism", text)
        self.assertIn("Never bag", text)

    def test_framework_has_kill_test(self) -> None:
        text = _read(FRAMEWORK)
        self.assertIn("If they say", text)
        self.assertIn("under ~40%", text)
        self.assertIn("Week 3", text)
        self.assertIn("ownership", text.lower())

    def test_subagent_exists(self) -> None:
        text = _read(AGENT)
        self.assertIn("name: fde-scoper", text)
        self.assertIn("fde-scoping", text)


class MeridianMemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.memo = _read(MEMO)
        cls.worked = _read(WORKED)
        cls.expected = json.loads(FIXTURE.read_text(encoding="utf-8"))["expected"]

    def test_addressed_to_vp(self) -> None:
        self.assertIn("VP of Engineering, Meridian Health", self.memo)

    def test_recommends_readiness_then_review(self) -> None:
        self.assertIn(self.expected["primary"], self.memo)
        self.assertIn(self.expected["secondary"], self.memo)
        self.assertIn("weeks 1–2", self.memo)
        self.assertIn("weeks 3–4", self.memo)
        self.assertIn(self.expected["kpi"], self.memo.lower())
        self.assertIn(self.expected["surface"], self.memo.lower())

    def test_names_mechanism(self) -> None:
        lowered = self.memo.lower()
        self.assertIn("does not mint reviewer hours", lowered)
        self.assertIn("minutes per pr", lowered)

    def test_rejects_required_alternatives(self) -> None:
        lowered = self.memo.lower()
        for name in self.expected["rejected"]:
            self.assertIn(name.lower(), lowered)

    def test_does_not_promise_a_percentage(self) -> None:
        self.assertTrue(self.expected["do_not_promise_pct"])
        self.assertNotRegex(self.memo, r"30%\s+off")
        self.assertIn("I will not pick the percentage", self.memo)

    def test_pushback_includes_spoken_line(self) -> None:
        self.assertIn("I'm not trying to slow cloud agents down", self.memo)
        self.assertIn("three to four weeks", self.memo)
        self.assertIn("nothing formal", self.memo)

    def test_three_kill_switch_questions(self) -> None:
        self.assertIn("Where do the four to five days actually go?", self.memo)
        self.assertIn("Is there more code to review than a year ago?", self.memo)
        self.assertIn("What does the 60% actually count?", self.memo)
        self.assertIn("this recommendation is wrong", self.memo)

    def test_week3_is_calibration_not_cycle_time(self) -> None:
        self.assertTrue(self.expected["week3_is_not_cycle_time"])
        self.assertIn("It is not a cycle-time story", self.memo)
        self.assertIn("The next team didn't need us", self.memo)

    def test_bear_case_has_early_signal(self) -> None:
        self.assertIn("week two", self.memo.lower())
        self.assertIn("ownership, not tooling", self.memo)

    def test_worked_example_matches_memo(self) -> None:
        self.assertIn("Enterprise Readiness (weeks 1–2) into Cursor Review and Bugbot (weeks 3–4)", self.worked)
        self.assertIn("time to first review", self.worked)


class MemoLengthTests(unittest.TestCase):
    def test_one_to_two_pages(self) -> None:
        words = len(re.findall(r"\b\w+\b", _read(MEMO)))
        # Spoken judgment, not a white paper. ~1–2 pages.
        self.assertGreater(words, 700, f"memo too short: {words} words")
        self.assertLess(words, 1600, f"memo too long for 1-2 pages: {words} words")


if __name__ == "__main__":
    unittest.main()
