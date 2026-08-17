---
name: elina-training
description: Guides Forward Deployed Engineering scoping for Cursor Review, Bugbot, and Enterprise Readiness engagements using the Meridian Health scoping memo. Use when the user mentions elina-training, scoping memos, Meridian Health, Review and Bugbot engagements, or engagement scoping.
disable-model-invocation: true
---

# Meridian Health — scoping memo

**To:** VP of Engineering, Meridian Health
**From:** Adrian Smitto, Forward Deployed Engineering
**Date:** August 13, 2026

Thanks for the half hour. Here's where I've landed, including a couple of places I'd push back.

The thing that stuck with me is that your adoption number hasn't moved in five months while your CTO is asking about cloud agents. I don't think those are the same problem, and I think the second one is downstream of the first. But you also gave me something more useful: a bottleneck with a number on it. Four to five days to get a PR through. That's what I want to aim the engagement at.

## What I'd do

The engagement is Cursor Review and Bugbot. Four weeks, because the first two are the foundation that makes the review work stick. Enterprise Readiness is that first half, not a second project. One number we're accountable for at the end, which is time to first review on two repos. I'll show full cycle time next to it, but the wait for a reviewer is the stage we're actually touching, and that's the one I'll put my name on. I won't pick the percentage in this memo. I'll pick it on the next call, once we know how much of the four to five days is actually the wait. If we can't beat the ninety-day baseline by the board meeting, the slide is the calibration ratio and an honest "too early," not a number we dressed up.

If you told me I could only have two weeks, I'd take Review, because it's the only piece your CTO can actually source in a board meeting — and I'd tell you I was trading away the foundation to hit a date.

Two teams, not the org. The council can come from the two that are already asking for SDK access. They're your most motivated senior people, and right now that motivation is aimed at building tools instead of at the thing slowing them down. The repos we put Review on should come from the cycle-time split, not from who asked. Highest volume, most concentrated reviewers, actual wait. Same two teams, fine. If not, we don't pick the wrong surface to keep fifteen people happy.

The council should be five to eight senior engineers, roughly four hours a week each, and I want both of the staff engineers who've been saying Cursor makes junior engineers worse, wherever they sit. You said you think they're partly right. I think they're describing a guardrails problem: juniors ship code they can't defend and seniors absorb the review cost. That's what rules and sub-agents are for. In my experience people stop arguing with rules they wrote, and working around the skeptics only leads to more problems.

A config repo with an owner. Not "some rules and a few sub-agents" nobody can locate. A named person and a real share of their week. Weeks one and two also include a test-scaffolding sub-agent, because it's one of the three things those engineers asked for and doesn't need a platform. If they hear "later" they'll keep asking for the SDK.

Then weeks three and four are Review and Bugbot deployed in your environment, tuned against what your own senior reviewers have actually written in PR comments, measured against ninety days of your own PR history. That means whoever actually reviews on those repos, two or three of your most senior, which may not be the council. I'd rather pull the history than spend week one watching a four-to-five day cycle produce a data point or two that won't survive a board member asking how we know. The one thing I need lined up before week three is somebody with authority over branch protection and review policy. That's a dependency, not a preference.

## What I considered instead

Cloud agents, which is what your CTO wants. An agent works off whatever conventions you hand it, and today nobody can tell me which of your rules are in use, so we'd be automating the inconsistency you already have.

SDK access, which is what your fifteen engineers want. Two of the three things they've asked for, code review and test scaffolding, don't need the SDK. The pipeline copilot probably doesn't either. And an internal platform needs a team that has already shipped one thing people use. We're not there yet.

Enterprise Readiness on its own. Right diagnosis, but it's one to two weeks, it leaves your review bottleneck where it is, and it gives the board nothing.

Review and Bugbot without the first two weeks. Would provide a usable number, but without a shared standard it would decay the same way the last set of rules did. That's my fallback if you cut me to two weeks, not my recommendation at four.

AI SDLC Integration is for orgs where Write and Review already work and the edges are disconnected. Write is the only stage you've started. Connecting Plan and Deploy would be stitching around a middle that isn't there yet.

## What I'd push back on

Three things, then one that's less comfortable.

On cloud agents, I wouldn't tell your CTO 'no'. Here's roughly what I'd say:

> "I'm not trying to slow down cloud agents, I'm trying to make them a smaller bet. An agent runs on whatever conventions we give it, and right now I can't tell you which of our rules are actually being used, so we'd be automating our inconsistency. Give me three weeks and I'll show you AI reviewing real PRs in our repos, against rules our own staff engineers wrote. Give me five and I'll have a measured change in how long that review takes. After that, cloud agents are the next engagement rather than a restart, and security will already have been through it, on a smaller surface than an agent committing code."

This gives him a date and a number instead of just a refusal, and the board ends up looking at your pull request process instead of somebody's sample repo. Worth saying that the follow-on is a three to four week engagement, so he doesn't hear 'small' and repeat it to the board. If we can get fifteen minutes of the next call with him on this sequence, week five isn't a surprise.

On the SDK, don't answer yet. Tell those engineers that code review and test scaffolding are shipping in the next four weeks — test scaffolding in the first two — and put them on the council that builds it. Whoever is still asking in month two is real demand worth scoping properly. If you grant it now you'll end up with fifteen one-off agents your platform team has to maintain.

On scope, four weeks will not move 4,000 engineers and I'm not going to pretend otherwise. It gets you one measured result and a pattern a third team can pick up without us. If the board is expecting an org-wide number in five weeks, tell me on the next call and not in week four.

As for security, "nothing formal" worries me. Informal concerns turn into formal blockers, and for a health tech company this size, having no written position on agents touching production code is itself worth knowing about. Review commenting on a PR is not the same thing as an agent committing to a production branch, and that's the distinction I'd want in front of them. What I need in week one is a carve-out list: patient data, production-path, anything under change control. Surfaces, not a process. If they can't name the surfaces, we don't put Review on production repos in week three and hope the conversation happens later.

## Three questions for the next call

Where do the four to five days actually go? Split it into PR open to first review, first review to approval, approval to merge. If the wait for first review is less than about 40% of the total, reviewer availability isn't your constraint and my recommendation is wrong. We'd be looking at release process, change control, CI, or PR size instead. I'd pull that split in week one rather than wait on it, so if it comes back against me we re-scope the second half then and not at the checkpoint. That's also how we pick the repos.

What are those two staff engineers actually seeing in the PRs? Specifically, is there more code to review now than a year ago? If juniors are dumping much larger diffs, compressing review without touching generation just relocates the problem, and cloud agents make it worse. In that case I keep the review half, but week two is PR-size hooks and a sub-agent that splits an oversized diff, not more style rules. If what they're seeing is code the author can't defend, that's still Review, and those two write the checklist the author has to answer before a human looks at it. Neither answer makes me want cloud agents first.

What does the 60% actually count, and can you pull two things before we talk: commit history on the platform team's rules for the last 90 days, and per-team active usage. Seats activated and engineers using agents daily are different populations. If the rules are real and a couple of teams are using them, the first half shrinks to about a week and we could decide where to spend the extra time. If there's nothing findable and no owner, then the handoff is the whole engagement and I'd narrow the review work to a single repo.

## Week three, and the board update

These are different slides, and I wouldn't mix them.

At the week three checkpoint, Review and Bugbot have just gone live on the repos we picked, plus the config repo with commits from your engineers. What you can actually show is whether your senior reviewers act on the comments or dismiss them, and how often the first pass catches what the human went on to flag independently. That ratio is the proof the tool is calibrated to your standards rather than to a vendor's. It is not a cycle-time story yet, and I wouldn't put one on the slide. If they're dismissing most of the comments, we don't expand, and the checkpoint is how we catch that before the board meeting.

The board is week five, which is after we've left. Time to first review against the ninety days of history is that slide. Even if it is a modest number, it's better than showing a large number from someone's benchmark. The rest of the slide is the third team. Week four they pick up the config repo and the review setup with us still there to watch. Week five they're running it without us. If that happens you're not reporting a successful pilot, you're reporting that the next team didn't need us, and those are quite different claims.

Two repos with real numbers and a third team running unattended is a better place to stand than an org-wide figure nobody can trace back to anything, even if it sounds nicer.

## The bear case

The likeliest way this fails is that I've misread the bottleneck. If most of your four to five days is queueing behind release trains, change control, or flaky CI, then we compress a stage that wasn't the problem, cycle time barely moves, and the board update reads as "we improved something adjacent." That's why the first question is so important.

The failure I'd watch harder is organizational. Flat at 60% for five months usually means nobody above the platform team is on the hook for adoption. If that's the case, we'll do great work on two teams but it will just stay with them, which is why I'd want you named as the owner of the adoption number rather than the platform team. Three signals in the first two weeks: whether your CTO gives me half an hour in week one — if he won't engage, then we have a problem; whether five council names volunteered or got assigned; and whether any director outside the two pilot teams asks to be next. If none of that has happened by the end of week two, we need to have a discussion about ownership.
