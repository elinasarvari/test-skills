# FDE scoping agent

A Cursor skill that helps a Forward Deployed Engineer do three things after an intro call: **understand the problem**, **align on it**, then **prescribe what Cursor can actually do** in the time they have.

It is not a sales script. The output is a 1–2 page memo a VP can forward to a CTO: the bottleneck you share, the Cursor-backed path, the alternatives that do not fit, pushback that keeps the relationship, questions that could change the plan, two different proofs, and a bear case.

## Run it as an FDE

In a new Agent chat, do this in order. Do not start with a product name.

**1. Align first**

```text
/fde-scoping

I am the FDE on this account, not the seller.
Before you recommend anything, restate the problem:
- who feels the pain
- what they asked for
- what the numbered bottleneck is
- which SDLC stage it lives in (Plan / Write / Review / Deploy)
- what we do not know yet

Stop there. Do not name a Cursor product until I confirm we are aligned.
```

Paste the call notes under that.

**2. Then map Cursor to that problem**

```text
We are aligned on: [the bottleneck you both accepted].
Now prescribe the smallest Cursor capability that can move that number
in [N] weeks. Reject the rest because they do not fit this problem,
not because they are worse products.
Write the 5-section memo to the person I spoke with.
```

You can also `@fde-scoper` with the same two-step prompt.

**3. Check the diagnosis, not the adjectives**

```bash
python3 -m fde_scoping.recommend tests/fixtures/meridian_health.json
```

If the memo names a different bottleneck than this output, the memo is wrong.

For **Meridian Health**, the aligned memo is already in `memos/meridian-health.md`. Use it. Do not re-trade the same facts.

For a **new customer**, the skill writes a new memo. It will not copy Meridian's sequence onto different facts.

## What Cursor can provide

| Path | Typical length | Fits when |
| --- | --- | --- |
| Enterprise Readiness | 1–2 weeks | Rolled out, no shared config, unknown rule usage, seniors say AI makes juniors worse |
| Cursor Review and Bugbot | 2–4 weeks | Review is a numbered bottleneck and you can name how comments change the wait |
| Cloud Agents | 3–4 week follow-on | A standard exists, security has a written position, agents can open PRs on a safe surface |
| SDK / internal agents | after one shipped internal tool | Demand remains after the packaged product covers the obvious jobs |
| AI SDLC Integration | later | Write and Review already work; Plan or Deploy is the disconnected edge |

Catalog and decision tests live in `.cursor/skills/fde-scoping/references/`.

## Meridian Health (the training scenario)

4,000-engineer healthcare company. Cursor at 60% and flat. No shared config. 4–5 day PR cycle. CTO wants cloud agents for a board update in five weeks. Fifteen seniors want the SDK. Two staff say Cursor makes juniors worse. Security is informal.

**Problem you align on:** reviewer wait, not "we need cloud agents."
**Cursor-backed path:** Enterprise Readiness (weeks 1–2) into Review and Bugbot (weeks 3–4). KPI is time to first review on two repos, percentage picked after the cycle-time split. Cloud agents and the SDK come after the standard exists.

## Tests

```bash
python3 -m unittest discover -s tests -v
```
