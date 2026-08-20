# What Cursor can provide

These are the time-boxed paths an FDE can staff. Products (rules, Bugbot, Cloud Agents, SDK) are ingredients. A path is a bet with an owner, a surface, and a number — not a pitch deck.

## Enterprise Readiness (1–2 weeks)

**What you do:** Find or create a versioned config repo (rules, skills, hooks, sub-agents). Name an owner with a real share of their week. Stand up a small council of senior engineers who write the first shared standard. Measure whether existing rules have commits and whether "adoption" means seats or daily agent use.

**Recommend when:** Cursor is already rolled out; rules/sub-agents exist but nobody can locate them; adoption flattened; seniors say AI makes juniors worse; no shared config repo.

**Cannot do:** Move PR cycle time. Give a CTO a board number. Fix org-wide adoption in two weeks.

**Typical output:** One config repo, named owner, 5–8 council members, a first useful sub-agent (often test scaffolding or a PR-size/diff-split helper), and a usage/ownership baseline.

## Cursor Review and Bugbot (2–4 weeks)

**What you do:** Turn on [Bugbot](https://cursor.com/docs/bugbot.md) / Cursor Review on a small set of repos. Calibrate comments against what the customer's own senior reviewers actually write. Measure time to first review and comment act-on vs dismiss rates against ~90 days of their PR history.

**Recommend when:** Review is the bottleneck with a number (days in review, reviewer queue, bounce rate). Write-stage conventions exist or you are pairing this with Readiness so they will.

**Cannot do:** Create reviewer hours if people simply never open the queue. Survive without a shared standard — comments decay into noise. Move 4,000 engineers in a month.

**Causal mechanism you must be able to name:**

1. **Cleaner intake** — authors fix what the bot flags before they request a human, so fewer PRs bounce and the queue is smaller.
2. **Higher throughput** — seniors spend fewer minutes per PR because the first pass is done, so the same scarce reviewers clear more.
3. **Not this:** redefining "first review" as the bot comment. Healthcare and most enterprises will not accept that definition for the board.

If the four-to-five days is calendar wait (reviewers in meetings, release trains, change control) and not effort or dirty diffs, this engagement is the wrong tool.

**Dependencies:** Branch-protection / review-policy owner before go-live. Carve-out list for patient data, production-path, and change-controlled surfaces. HIPAA BAA / Privacy Mode check for health tech.

## Cloud Agents (follow-on, typically 3–4 weeks)

**What you do:** Give agents an environment that can build, test, and open PRs — [environment setup](https://cursor.com/docs/cloud-agent.md) is "giving the agent a computer." Point them at conventions the org already uses. Start on a small, non-production-path surface.

**Recommend when:** A shared standard exists and is in use; security has a written position on agents writing code; the customer can name repos that are safe to touch; someone will review agent PRs.

**Reject when:** Rules are unfindable, nobody owns config, security is "nothing formal," or the sponsor wants a board demo more than a measured loop. An agent on inconsistent conventions automates the inconsistency.

**Healthcare note:** Review commenting on a diff is a smaller surface than an agent committing. Sequence Review first so security has already seen AI on real PRs.

## SDK / internal agents

**What you do:** Help a platform team build first-party agents (review, test scaffolding, pipeline copilots) on the Cursor SDK.

**Recommend when:** A team has already shipped one thing people use, there is a named platform owner, and demand is still there after the packaged product covers the obvious jobs.

**Reject when:** Fifteen seniors want to build the thing you are about to ship as a product. Granting SDK access then means you own fifteen one-off agents. Code review and test scaffolding do not need the SDK. A pipeline copilot might — later.

## AI SDLC Integration (Plan / Write / Review / Deploy)

**What you do:** Connect stages that already work so context flows (ticket → agent → PR → release) instead of living in one island.

**Recommend when:** Write and Review already work and the pain is the edges (planning artifacts ignored, deploy disconnected, no handoff).

**Reject when:** Only Write has started. Stitching Plan and Deploy around a missing Review middle is theater.

## Sequencing patterns

| Situation | Pattern |
| --- | --- |
| Rolled out, no standard, review is the numbered bottleneck, board in ~5 weeks | Readiness (weeks 1–2) into Review/Bugbot (weeks 3–4) |
| Standard exists and is used, review is the bottleneck | Review/Bugbot only |
| Standard missing, no numbered bottleneck, no board date | Readiness only |
| Standard + Review working, sponsor wants autonomy | Cloud Agents as the next engagement |
| Platform already shipped one used internal tool | SDK scope |

Never bag "all of the above" into one four-week path.
