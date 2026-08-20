# Worked example — Meridian Health

Use these facts and this recommendation when the user asks for the Meridian Health memo. Do not re-trade the engagement on the same facts.

## Facts from the 30-minute intro (VP of Engineering)

- 4,000-engineer healthcare technology company.
- Cursor rolled out company-wide six months ago. Adoption hit 60% in month one and has been flat since. PR velocity has not moved.
- Platform team built "some rules and a few sub-agents." VP does not know if they are used. No shared config repo.
- CTO saw a vendor demo and is asking why they are not running cloud agents. Wants something demonstrable for a board update five weeks out. Week-3 customer checkpoint exists.
- PR review cycle is 4–5 days end to end. VP says reviewer availability is the constraint, not code quality.
- Two senior staff engineers have said publicly that Cursor "makes junior engineers worse." VP thinks they are partially right.
- Security flagged a concern about agents touching production code. Nothing formal.
- ~15 senior engineers across two teams want SDK access to build internal agents for code review, test scaffolding, and a pipeline copilot. VP is unsure how to respond.
- Budget: 4-week engagement. She wants a recommendation, the reasoning, and a sense of what is possible before the board update.

## Recommendation (do not deviate on these facts)

**Enterprise Readiness (weeks 1–2) into Cursor Review and Bugbot (weeks 3–4).** One engagement, four weeks, two teams / two repos. The number you put your name on is **time to first review** against ninety days of their PR history. Show full cycle time next to it. Do not pick the percentage in the memo — pick it on the next call after the cycle-time split.

**Mechanism:** Review does not mint reviewer hours. It (1) lets authors clear bot findings before they request a human, so fewer dirty PRs enter a scarce queue, and (2) cuts minutes-per-PR so the same reviewers clear more. If the 4–5 days is calendar unavailability, release trains, or change control, this bet is wrong — that is why question one exists and is answered in week one.

**Council:** 5–8 seniors, ~4 hours/week, drawn from the two teams already asking for the SDK. Both staff skeptics sit on it. They write the rules and the author-defense checklist. A test-scaffolding sub-agent ships in weeks 1–2 because it is one of the three things those engineers asked for and does not need a platform.

**Repos:** picked from the cycle-time split (volume, concentrated reviewers, actual wait), not from who asked. Named config-repo owner. VP owns the success number. Branch-protection authority before week three.

## Alternatives and why they lose

| Alternative | Why reject |
| --- | --- |
| Cloud Agents now | No findable standard, no owner, informal security. Automates inconsistency. Sequence after Review so security has seen AI on real PRs. Follow-on is 3–4 weeks, not "small." |
| SDK now | Two of the three asks (review, test scaffolding) ship in this engagement without the SDK. Granting it now = fifteen one-off agents. Whoever still asks in month two is real demand. |
| Readiness alone | Right diagnosis, no board number, leaves the 4–5 day review where it is. |
| Review/Bugbot without weeks 1–2 | A number that decays the way the last rules did. Fallback if cut to two weeks — take Review and say you traded away the foundation. |
| AI SDLC Integration | Write is the only stage they have started. Connecting Plan and Deploy would stitch around a missing middle. |
| Org-wide adoption push | Four weeks will not move 4,000 engineers. Flat 60% is an ownership problem. This engagement is not an adoption campaign. |

## Pushback lines

Cloud agents — see the spoken paragraph in the submit memo. Include "three to four week follow-on" so the CTO does not hear "small" and repeat it to the board.

SDK — don't answer. Put them on the council. Ship review and test scaffolding.

Security — "nothing formal" is the finding. Carve-out list week one: patient data, production-path, change control. Confirm BAA / Privacy Mode. Review comments ≠ commits to a production branch.

Scope — two teams, not the org. If the board expects org-wide, learn that next call.

## Three questions (each can change the rec)

1. **Where do the 4–5 days go?** Open → first review → approval → merge, and is the wait effort or calendar? If first-review wait is under ~40%, or it is calendar/release/CI, Review is the wrong tool — re-scope the second half in week one.
2. **Is there more code to review than a year ago?** If juniors dump much larger diffs, week two becomes PR-size hooks and a diff-splitting sub-agent, not more style rules. If authors can't defend the code, those two staff write the pre-human checklist. Neither answer makes cloud agents first.
3. **What does 60% count, and can you pull 90-day rule-commit history plus per-team active use?** Seats ≠ daily agents. If rules are real, shrink Readiness to a week. If nothing is findable, the handoff is the engagement and Review narrows to one repo.

## Week 3 vs week 5

- **Week 3:** Review live; config repo has their commits. Show act-on vs dismiss and overlap with what humans flag independently. Proves calibration to Meridian's standard. Not a cycle-time story. If they dismiss most comments, do not expand.
- **Week 5 (board):** Time to first review vs 90-day baseline, sample stated (two weeks of PRs, two repos). If you have not beaten it, calibration + "too early." Second half of the slide: a third team running the setup unattended. "The next team didn't need us" beats "the pilot went well."

## Bear case

Likeliest miss: the 4–5 days is not reviewer effort. Early signal: the week-one split. Org miss: nobody above platform owns adoption. Signals by end of week two: CTO gave 30 minutes; council names volunteered vs assigned; a director outside the two teams asked to be next. If none of that happened, the conversation is ownership, not tooling.
