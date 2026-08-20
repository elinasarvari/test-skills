"""Pick a Cursor engagement from structured intro-call facts.

This is the judgment skeleton the skill writes into a memo. It does not
draft prose. It aligns on the bottleneck first and refuses to treat a
sponsor ask as the problem.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Recommendation:
    primary: str
    secondary: str | None
    kpi: str | None
    surface: str
    rejected: list[str]
    reasons: list[str]
    pushback: list[str]
    kill_questions: list[str]
    week3_proof: str
    board_proof: str
    bear_case: str
    early_signal: str


def recommend(facts: dict[str, Any]) -> Recommendation:
    """Return an engagement bet from intro-call facts.

    Expected keys are documented in tests/fixtures/meridian_health.json.
    Unknown keys are ignored. Missing keys default to the conservative
    (foundation-first) path.
    """
    shared_config = bool(facts.get("shared_config_repo"))
    rules_known = bool(facts.get("rules_usage_known"))
    review_days = facts.get("pr_cycle_days") or []
    has_review_number = bool(review_days) or bool(facts.get("stated_constraint"))
    constraint = facts.get("stated_constraint")
    write_started = facts.get("write_stage_started", True)
    review_works = bool(facts.get("review_stage_works"))
    security_formal = bool(facts.get("security_formal"))
    cto_wants = facts.get("cto_wants")
    sdk_askers = int(facts.get("sdk_askers") or 0)
    budget_weeks = int(facts.get("budget_weeks") or 4)
    board_weeks = facts.get("board_weeks_out")
    engineers = int(facts.get("engineers") or 0)
    adoption_flat = int(facts.get("adoption_flat_months") or 0)

    rejected = [
        "AI SDLC Integration",
        "org-wide adoption push",
        "SDK now",
        "Cloud Agents now",
    ]
    reasons: list[str] = []
    pushback: list[str] = []

    if engineers and engineers > 200 and budget_weeks <= 4:
        reasons.append("Four weeks will not move an org this size. Pilot a measurable surface.")
    if not review_works and write_started:
        rejected = [r for r in rejected if r != "AI SDLC Integration"] + ["AI SDLC Integration"]
        reasons.append("Write is started and Review is not. Do not stitch Plan/Deploy around a missing middle.")
    if sdk_askers and not facts.get("internal_tool_already_shipped"):
        reasons.append("SDK demand before one shipped internal tool is a pile of one-offs. Absorb the askers.")
        pushback.append("Do not grant SDK access yet. Ship review and test scaffolding; put askers on the council.")
    if cto_wants == "cloud_agents" and (not shared_config or not rules_known or not security_formal):
        reasons.append("Cloud agents run on conventions you cannot currently name. Sequence them after a standard exists.")
        pushback.append("Do not say no to cloud agents. Make them a 3-4 week follow-on after Review is live on real PRs.")
    if not security_formal:
        pushback.append("Informal security concern is the finding. Carve-out list in week one. Review comments are not prod commits.")
    if adoption_flat >= 3:
        reasons.append("Flat adoption is usually ownership, not missing features. This is not an adoption campaign.")

    foundation_missing = (not shared_config) or (not rules_known)
    review_is_the_bet = has_review_number and constraint in {None, "reviewer_availability", "review_cycle"}

    if foundation_missing and review_is_the_bet and budget_weeks >= 4:
        primary = "Enterprise Readiness"
        secondary = "Cursor Review and Bugbot"
        kpi = "time to first review"
        surface = "two teams"
        reasons.append("Need a versioned standard before Review will stick, and a numbered review bottleneck to aim at.")
        rejected = [
            "Cloud Agents now",
            "SDK now",
            "Enterprise Readiness alone",
            "Review and Bugbot without foundation",
            "AI SDLC Integration",
            "org-wide adoption push",
        ]
        week3 = "Review live; customer commits on the config repo; act-on vs dismiss and overlap with human flags."
        board = "Time to first review vs 90-day baseline on a stated sample, plus a third team running unattended."
        bear = "The cycle-time number is not reviewer effort (release train, change control, CI), or nobody above platform owns the outcome."
        signal = "Week-one cycle-time split undercuts reviewer wait; or by week two no CTO time, assigned-only council, no outside director asking to be next."
    elif review_is_the_bet and not foundation_missing:
        primary = "Cursor Review and Bugbot"
        secondary = None
        kpi = "time to first review"
        surface = "two teams"
        reasons.append("A used standard already exists. Spend the window on the numbered review bottleneck.")
        rejected = [
            "Enterprise Readiness",
            "Cloud Agents now",
            "SDK now",
            "AI SDLC Integration",
            "org-wide adoption push",
        ]
        week3 = "Act-on vs dismiss and overlap with human flags on the pilot repos."
        board = "Time to first review vs 90-day baseline on a stated sample."
        bear = "Wait is calendar or release process, not reviewer effort."
        signal = "Week-one split shows first-review wait under ~40% of cycle time."
    elif foundation_missing:
        primary = "Enterprise Readiness"
        secondary = None
        kpi = None
        surface = "one config repo and a named owner"
        reasons.append("No numbered bottleneck we can honestly aim a product at. Diagnose and install a standard.")
        rejected = [
            "Cursor Review and Bugbot",
            "Cloud Agents now",
            "SDK now",
            "AI SDLC Integration",
            "org-wide adoption push",
        ]
        week3 = "Config repo has customer commits and a named owner. Usage definition (seats vs daily agents) is settled."
        board = "Do not promise a cycle-time number. Show the standard and who owns it."
        bear = "Handoff is the whole engagement and nobody will own the repo after week two."
        signal = "No owner named, no council volunteers, rules still unfindable."
    elif review_works and write_started and facts.get("edges_disconnected"):
        primary = "AI SDLC Integration"
        secondary = None
        kpi = facts.get("edge_kpi") or "handoff latency between stages"
        surface = "one connected path"
        rejected = [
            "Enterprise Readiness",
            "Cursor Review and Bugbot",
            "Cloud Agents now",
            "SDK now",
        ]
        week3 = "One ticket-to-PR-to-release path carrying shared context."
        board = "A measured handoff, not a new island."
        bear = "The edges were not the problem; Write or Review still broken."
        signal = "Week one shows Review or Write still failing on the chosen path."
    elif shared_config and rules_known and security_formal and cto_wants == "cloud_agents":
        primary = "Cloud Agents"
        secondary = None
        kpi = "agent PRs merged on a named safe surface"
        surface = "one non-production-path repo"
        rejected = [
            "Enterprise Readiness",
            "SDK now",
            "AI SDLC Integration",
        ]
        week3 = "Environment can build and test; first agent PR on the carve-out-approved repo."
        board = "Agent-opened PRs on their repo, not a vendor demo."
        bear = "Security retracts the carve-out, or the environment cannot close a loop."
        signal = "Week one: no written surfaces, or environment cannot run tests."
    else:
        primary = "Enterprise Readiness"
        secondary = None
        kpi = None
        surface = "diagnosis"
        week3 = "Named owner, versioned config, settled usage definition."
        board = "Honesty about what is not yet measurable."
        bear = "We picked a product before we had a bottleneck."
        signal = "Facts still do not support a numbered bet by the end of week one."

    if board_weeks and board_weeks <= 5 and primary == "Enterprise Readiness" and secondary is None:
        reasons.append("A board date with Readiness alone will not produce a customer-owned cycle-time number. Say that now.")

    kill_questions = [
        "Where does cycle time actually go (open → first review → approval → merge), and is the wait effort or calendar?",
        "Is there more code to review than a year ago (diff size / author defense)?",
        "What does the adoption number count, and do existing rules have real commits and an owner?",
    ]

    return Recommendation(
        primary=primary,
        secondary=secondary,
        kpi=kpi,
        surface=surface,
        rejected=rejected,
        reasons=reasons,
        pushback=pushback,
        kill_questions=kill_questions,
        week3_proof=week3,
        board_proof=board,
        bear_case=bear,
        early_signal=signal,
    )


def as_dict(rec: Recommendation) -> dict[str, Any]:
    return rec.__dict__.copy()


def main(argv: list[str] | None = None) -> int:
    import json
    import sys
    from pathlib import Path

    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("usage: python3 -m fde_scoping.recommend <facts.json>", file=sys.stderr)
        return 2
    payload = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    facts = payload["facts"] if "facts" in payload else payload
    rec = recommend(facts)
    print(json.dumps(as_dict(rec), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

