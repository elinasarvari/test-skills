# FDE scoping agent

A Cursor skill and subagent that turns a short intro-call brief into a 1–2 page engagement scoping memo. Built so Elina (or anyone else) can paste a new customer scenario and get a recommendation with the same judgment bar: smallest bet that can move a numbered bottleneck, named alternatives, relationship-safe pushback, kill-switch questions, two different proofs, and a bear case.

## How to use it

In Cursor Agent chat:

- `/fde-scoping` plus the call notes, or
- `@fde-scoper` and paste the scenario, or
- mention Meridian Health / scoping memo — the skill should attach on its own.

For **Meridian Health**, do not re-trade the call. Use `memos/meridian-health.md`. That is the submit-ready memo for the VP of Engineering.

For a **new customer**, the agent follows `.cursor/skills/fde-scoping/SKILL.md` and writes a new memo. It will not copy Meridian's sequence onto different facts.

## What it knows how to sell

| Engagement | Typical length | Use when |
| --- | --- | --- |
| Enterprise Readiness | 1–2 weeks | Rolled out, no shared config, unknown rule usage, seniors say AI makes juniors worse |
| Cursor Review and Bugbot | 2–4 weeks | Review is a numbered bottleneck and you can name how comments change the wait |
| Cloud Agents | 3–4 week follow-on | A standard exists, security has a written position, agents can open PRs on a safe surface |
| SDK / internal agents | after one shipped internal tool | Demand remains after the packaged product covers the obvious jobs |
| AI SDLC Integration | later | Write and Review already work; Plan or Deploy is the disconnected edge |

Catalog and decision tests live in `.cursor/skills/fde-scoping/references/`.

## Meridian Health (the training scenario)

4,000-engineer healthcare company. Cursor at 60% and flat. No shared config. 4–5 day PR cycle. CTO wants cloud agents for a board update in five weeks. Fifteen seniors want the SDK. Two staff say Cursor makes juniors worse. Security is informal.

**Recommendation:** Enterprise Readiness (weeks 1–2) into Review and Bugbot (weeks 3–4). KPI is time to first review on two repos, percentage picked after the cycle-time split. Cloud agents and the SDK are sequenced, not granted.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

Score a structured brief (no prose):

```bash
python3 -m fde_scoping.recommend tests/fixtures/meridian_health.json
```
