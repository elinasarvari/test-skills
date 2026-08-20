# Decision framework

## 1. Split the conversation into three piles

| Pile | Examples | How to treat it |
| --- | --- | --- |
| **Ask** | "Why aren't we on cloud agents?" "Give the 15 people the SDK." | Sequence or absorb. Do not let it pick the engagement. |
| **Symptom** | Adoption flat at 60%. "Cursor makes juniors worse." | Diagnose. Often Write-stage guardrails or ownership. |
| **Bottleneck with a number** | 4–5 day PR cycle. Reviewer wait. Bounce rate. | Aim here if you can name a mechanism. |

If you only have symptoms and asks, the engagement is diagnosis (Readiness), not a board number.

## 2. Test the bottleneck

A number is not a diagnosis. Split cycle time before you bet Review:

- Open → first review
- First review → approval
- Approval → merge

**Kill:** if wait-for-first-review is under ~40% of the total, reviewer availability is not the constraint. Look at release trains, change control, CI, or PR size.

Also ask whether **reviewer effort** or **calendar unavailability** dominates. Bugbot helps effort and dirty first diffs. It does not create hours on a calendar.

Ask whether there is **more code to review than a year ago**. If juniors ship much larger diffs, compressing review relocates the problem. Then week two is PR-size hooks and a diff-splitting sub-agent, not more style rules.

## 3. Test the foundation

Before Cloud Agents or a durable Review install:

- Is there a shared, versioned config repo?
- Does it have commits in the last 90 days?
- Who owns it, with what fraction of their week?
- What does "60% adoption" count — seats activated, or engineers using agents daily?

**If rules are real and used:** shrink Readiness toward a week and spend the rest on Review.
**If nothing is findable and no one owns it:** the handoff *is* the engagement. Narrow Review to one repo, or drop the board-number promise.

## 4. Design the pilot surface

- Two teams, not the org. Four weeks will not move thousands of engineers.
- Pick repos from the cycle-time split (highest volume, most concentrated reviewers, actual wait) — not from who asked for the SDK.
- Council of 5–8 seniors, ~4 hours/week. Put public skeptics on it. People stop arguing with rules they wrote.
- Named owner of the config repo. Named owner of the success number (usually the VP, not the platform team).
- Branch-protection authority lined up before Review week.

## 5. Phrase pushback so it keeps the relationship

**Cloud agents (sponsor ask):** not a no. Make it a smaller next bet.

> I'm not trying to slow cloud agents down. I'm trying to make them a smaller bet. An agent runs on whatever conventions we give it, and right now I can't tell you which rules are in use. Give me three weeks and I'll show AI reviewing real PRs against rules your staff engineers wrote. Give me five and I'll have a number on how long review takes. Then cloud agents are the next engagement — say three to four weeks, not "small" — not a restart.

**SDK (grassroots ask):** don't answer yet. Ship the two jobs that don't need it (review, test scaffolding). Put the askers on the council. Whoever is still asking in month two is real demand.

**Scope:** say out loud that four weeks will not move the whole org. If the board expects an org-wide number, learn that on the next call, not in week four.

**Security, especially health tech:** "nothing formal" is the finding. Get a carve-out list in week one (patient data, production-path, change control). Confirm BAA / Privacy Mode before anyone assumes PHI is in scope. Review-on-PR is the smaller surface; use that to walk security in before agents write code.

## 6. Two proofs, two slides

| When | Demonstrable thing | What it proves | What it does not prove |
| --- | --- | --- | --- |
| Week 3 checkpoint | Review live; config repo has customer commits; act-on vs dismiss; overlap with what humans flag independently | Calibration to *their* standard | Cycle time |
| Board (week 4–5) | Time to first review vs 90-day baseline on a stated sample (e.g. two weeks of PRs on two repos). Plus a third team running the setup unattended. | A customer-owned number, and that the pattern transfers | Org-wide adoption |

If reviewers dismiss most comments at week 3, do not expand, and do not take a cycle-time slide to the board. If you have not beaten the baseline by week 5, the slide is the calibration ratio and "too early."

"The next team didn't need us" is a better board claim than "the pilot went well."

## 7. Bear case patterns

| Failure | Early signal (week 1–2) | Conversation it forces |
| --- | --- | --- |
| Misread bottleneck (release train, change control, flaky CI) | Open→first-review is a small slice of the 4–5 days | Re-scope off Review; do not take a vanity adjacent metric to the board |
| Dirty generation, not slow review | Diffs much larger than a year ago; seniors complain authors can't defend the code | Keep Review; spend week two on PR-size hooks and an author checklist, not more style rules |
| No owner above platform | CTO won't give 30 minutes; council names get assigned, not volunteered; no director outside the pilot asks to be next | Ownership conversation, not tooling |
| Security freeze | No carve-out list; security won't distinguish comment-on-PR from commit-to-prod | Stay off production-path repos; slip Review rather than surprise them |
| Foundation is vapor | No findable rules, no owner, 60% is seats not use | Narrow to one repo or drop the board-number promise |

## 8. Question test

A discovery question is good only if you can finish this sentence:

> If they say ____, I change the recommendation to ____.

If you cannot, rewrite the question.
