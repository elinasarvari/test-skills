# Meridian Health — scoping memo

**To:** VP of Engineering, Meridian Health
**From:** Elina Sarvari, Forward Deployed Engineering
**Date:** August 20, 2026

Thanks for the half hour. I want to make sure we are aimed at the same problem before I talk about Cursor.

Three conversations are running as if they were one. Adoption has been flat at 60% for five months. Your CTO wants cloud agents because he saw a demo. Neither is the problem I think we should work. You have a bottleneck with a number: four to five days to get a PR through, and you said reviewer availability is the constraint. That is the issue I would spend four weeks on — if the split confirms it. The rest of this memo is the Cursor-backed path for that issue, not a response to the demo.

## 1. Recommendation, and the alternatives I rejected

**Enterprise Readiness (weeks 1–2) into Cursor Review and Bugbot (weeks 3–4).** One engagement, four weeks, two teams, two repos. The number I will put my name on is time to first review against ninety days of your own PR history. I will show full cycle time next to it, but the stage this work can touch is the wait for a reviewer.

I will not pick the percentage in this memo. I will pick it on the next call, once we know how much of the four to five days is actually that wait. If we cannot beat the baseline by the board meeting, the slide is the calibration ratio and an honest "too early."

Review does not mint reviewer hours. Authors clear bot findings before they request a human, so fewer dirty PRs enter a scarce queue. Seniors spend fewer minutes per PR because the first pass is done, so the same reviewers clear more. If the four to five days is people in meetings, a release train, or change control, this bet is wrong. That is why question one is answered in week one, before Review goes live.

Two teams, not 4,000 engineers. The council comes from the two teams already asking for SDK access: five to eight seniors, about four hours a week. Both staff engineers who said Cursor makes juniors worse sit on it. You think they are partly right. They are describing a guardrails problem — juniors ship code they cannot defend, seniors absorb the cost. People stop arguing with rules they wrote.

A config repo with a named owner and a real share of their week. Not "some rules and a few sub-agents" nobody can locate. Weeks one and two also ship a test-scaffolding sub-agent, one of the three things those fifteen asked for, and it does not need a platform.

Repos get picked from the cycle-time split — volume, concentrated reviewers, actual wait — not from who asked. Before week three I need someone with authority over branch protection. You own the success number. The platform team should not.

If you could only give me two weeks, I would take Review, because it is the only piece your CTO can source in a board meeting, and I would tell you I was trading away the foundation.

**Also considered:**

- **Cloud Agents now** — what your CTO wants. An agent runs on the conventions you hand it. Today nobody can tell me which rules are in use, so we would automate the inconsistency you already have.
- **SDK now** — what the fifteen want. Code review and test scaffolding do not need the SDK. Grant it now and you own fifteen one-off agents. An internal platform needs a team that has already shipped one thing people use.
- **Enterprise Readiness alone** — right diagnosis. Leaves the four-to-five-day review where it is and gives the board nothing.
- **Review and Bugbot without foundation** — a usable number that decays the way the last rules did. Fallback at two weeks, not the recommendation at four.
- **AI SDLC Integration** — for orgs where Write and Review already work. Write is the only stage you have started.
- **An org-wide adoption push** — four weeks will not move 4,000 engineers. A flat 60% is usually an ownership problem. This engagement is not an adoption campaign.

## 2. What I would push back on

On cloud agents I would not tell your CTO no. I would say:

> I'm not trying to slow cloud agents down. I'm trying to make them a smaller bet. An agent runs on whatever conventions we give it, and right now I can't tell you which of our rules are actually in use. Give me three weeks and I'll show AI reviewing real PRs against rules our own staff engineers wrote. Give me five and I'll have a number on how long that review takes. Then cloud agents are the next engagement — three to four weeks, not a restart — and security will already have seen AI on a smaller surface than an agent committing code.

Say the follow-on is three to four weeks so he does not hear "small" and repeat that to the board. Fifteen minutes with him on the next call means week five is not a surprise.

On the SDK, do not answer yet. Tell those fifteen that code review and test scaffolding ship in the next four weeks — test scaffolding in the first two — and put them on the council. Whoever is still asking in month two is real demand.

On scope: if the board expects an org-wide number in five weeks, tell me on the next call, not in week four.

On security, "nothing formal" is the finding. For health tech at your size, no written position on agents touching production code is itself worth escalating. Review commenting on a PR is not an agent committing to a production branch. Week one I need a carve-out list — patient data, production-path, anything under change control — and a straight answer on BAA / Privacy Mode before anyone assumes PHI is in scope. If they cannot name the surfaces, we do not put Review on production repos in week three.

## 3. Three questions for the next call

**Where do the four to five days actually go?** Open to first review, first review to approval, approval to merge — and is that wait effort or calendar? If the wait for first review is under about 40% of the total, reviewer availability is not your constraint and this recommendation is wrong. We would be looking at release process, change control, CI, or PR size, and I would re-scope the second half in week one. That split is also how we pick the repos.

**Is there more code to review than a year ago?** If juniors are shipping much larger diffs, compressing review relocates the problem, and cloud agents make it worse. Then I keep Review, but week two is PR-size hooks and a diff-splitting sub-agent, not more style rules. If those two staff are seeing code the author cannot defend, they write the checklist the author answers before a human looks. Neither answer makes me want cloud agents first.

**What does the 60% actually count?** Pull two things before we talk: 90-day commit history on the platform team's rules, and per-team active usage. Seats and daily agent users are different populations. If the rules are real, the first half shrinks to about a week. If nothing is findable and no one owns it, the handoff is the engagement and I would narrow Review to one repo.

## 4. Week 3 versus the board update

These are different slides.

**Week 3.** Review is live. The config repo has commits from your engineers. What you show is whether senior reviewers act on the comments or dismiss them, and how often the first pass catches what the human flagged independently. That ratio proves calibration to Meridian's standards, not a vendor's. It is not a cycle-time story. If they dismiss most comments, we do not expand — and we have caught it before the board.

**Week 5.** Time to first review against the ninety-day baseline, sample stated: two weeks of PRs on two repos. If we have not beaten it, the slide is the calibration ratio and "too early." The other half is a third team running the setup unattended. Week four they pick it up with us watching. Week five they run it without us. "The next team didn't need us" is a better claim than "the pilot went well."

## 5. The bear case

The likeliest miss is that I have misread the bottleneck. If most of the four to five days is queueing behind release trains, change control, or flaky CI, we compress a stage that was not the problem and the board hears "we improved something adjacent." That is why question one is answered in week one.

The failure I would watch harder is organizational. Flat at 60% for five months usually means nobody above the platform team owns adoption. We can do good work on two teams and it stays there. I want you named as the owner of that number. Three signals by the end of week two: whether your CTO gave me half an hour; whether council names volunteered or got assigned; and whether any director outside the two pilot teams asked to be next. If none of that happened, the conversation we need is about ownership, not tooling.
