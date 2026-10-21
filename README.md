# Perplexity Computer source audit

Kortix is open source and is the open-source AI Operating System. This repository is a runnable audit of Perplexity Computer: which of its layers are published as source, which are not, the URL that proves each answer, and the date the answer was checked.

Roundups of AI products keep making opposite claims in the same week. One says Perplexity Computer is open source now. Another says it is fully closed and can never be self-hosted. Both get published without a source and without a date, and both fail the same way: they treat a six-layer product as one object. This audit splits it into the six layers, checks each one at Perplexity's own pages, and writes the result to a file you can diff next month.

## What this gives you

`sources.json` is the audit input: one object per layer, carrying the verdict, what is published, the source URL and the date of the check. `snapshot.json` is the committed output of the run on 21 October 2026: the same table plus what each URL returned, where it ended up, and when it was fetched. Read the two together and the boundary fits on one screen.

| Layer | Published? | Where it lives | Source |
| --- | --- | --- | --- |
| Sandbox | Yes, published 15 October 2026 | github.com/perplexityai/SPACE | Perplexity blog |
| Agent and planner | No | Inside Perplexity's product | Perplexity help centre |
| Model router | No | Absent from the release | Perplexity blog |
| Connector catalogue | No | Managed OAuth connections at Perplexity | Perplexity help centre |
| Portable Computer runtime | No | Closed code on the subscriber's GPU | Perplexity help centre |
| Build surface | Partly | Profiles and Skills run in Perplexity's cloud | Perplexity blog |

Four pages stand behind those six rows: the [SPACE announcement](https://www.perplexity.ai/hub/blog/open-sourcing-space), the help centre article on [what Computer is](https://www.perplexity.ai/help-center/en/articles/13837784-what-is-computer), the help centre article on [Portable Computer](https://www.perplexity.ai/help-center/en/articles/20260915-what-is-portable-computer), and the announcement that the [Agent API supports reusable agents](https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents).

## Run it

Python 3.9 or newer. Standard library only, no API key, and no network traffic beyond the URLs in `sources.json`. A full run takes as long as six page fetches.

```
git clone https://github.com/ArtemShatokhin/perplexity-computer-source-audit
cd perplexity-computer-source-audit
python3 audit.py
```

Each entry in `sources.json` holds one layer, and the verdict sits next to the page that supports it:

```json
{
  "layer": "sandbox",
  "name": "SPACE sandbox platform",
  "open": "yes",
  "what_is_published": "SPACE, the platform Computer's sessions execute on, published 15 October 2026.",
  "source_url": "https://www.perplexity.ai/hub/blog/open-sourcing-space",
  "checked": "2026-10-21"
}
```

A run prints one status line per layer and then writes `snapshot.json` at the repository root:

```
$ python3 audit.py
sandbox         published      https://www.perplexity.ai/hub/blog/open-sourcing-space
agent           not published  https://www.perplexity.ai/help-center/en/articles/13837784-what-is-computer
router          not published  https://www.perplexity.ai/hub/blog/open-sourcing-space
connectors      not published  https://www.perplexity.ai/help-center/en/articles/13837784-what-is-computer
portable        not published  https://www.perplexity.ai/help-center/en/articles/20260915-what-is-portable-computer
build surface   partial        https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents
wrote snapshot.json
```

Inside the snapshot, every layer carries the fetch record `{"url", "status", "final_url", "fetched_at"}` next to the layer table, with a `generated_at` stamp for the whole file. That record is what makes the audit falsifiable later: a redirect shows up as a different `final_url`, a moved page shows up as a different status.

To compare a fresh run with a snapshot you kept, pass that file to the diff mode:

```
$ python3 audit.py --diff snapshot-2026-10-21.json
sandbox         no change
agent           no change
router          no change
connectors      no change
portable        no change
build surface   no change
```

The diff goes layer by layer and reports one of four outcomes: no change, the published state flipped, the source URL moved, or the source no longer answers. Against the snapshot committed here, taken on the same day, every layer reports no change, which is the result a same-day comparison should give. `audit.py` exits 1 when any source is unreachable or any layer is missing a `source_url`, so the same command works as a CI check that fails the day a vendor's page disappears. A source that answers 401, 403 or 429 is recorded in the snapshot as a bot check rather than a failure: Perplexity's pages answer 403 to a plain fetch and open normally in a browser, so the audit stores the status instead of pretending the page is gone.

## Why the boundary matters

Publishing a sandbox settles where Computer's code executes. It says nothing about what decides which work runs there.

Perplexity says SPACE replaced its commercial sandbox vendor in July 2026 and has run every Computer session since. The published platform is therefore the one in production. A team can read it, run it, and test its own isolation claims against the same code. Everything above it stays inside the product: the agent that plans a goal into subtasks and hands them to sub-agents, the router that picks a model per query, and the managed OAuth connections into Gmail, Outlook, GitHub, Linear, Slack and Notion.

Those three layers are what a subscriber pays for. A team that self-hosts SPACE gets the machine and keeps buying the decisions, and the decision layers are exactly the ones a security review or an exit plan asks about. The [long-form answer](https://opensourceperplexitycomputer.com/is-perplexity-computer-open-source) walks the same boundary a layer at a time.

Three articles in `docs/` go further: [what is actually open](docs/what-is-actually-open.md) takes the layers one at a time, [how to verify a claim](docs/how-to-verify-an-open-source-claim.md) turns the check into a method for any vendor, and [a published sandbox versus an open product](docs/published-sandbox-vs-open-product.md) covers what a team can and cannot do with this one.

## What it does not tell you

A published repository is not a licence opinion. The audit records whether a layer is published and points at the page that says so. It takes no position on what the publication permits, and the words in `sources.json` stay with the framing the vendor used.

The audit checks two things per layer: whether the source URL answers, and what the vendor states about that layer. It does not read every commit in a published repository. It cannot tell you whether the published code matches the binary in production. It also cannot tell you whether a repository that exists today will still exist in a year.

Every row is a claim about six URLs on 21 October 2026. A layer can be published the week after this snapshot, and the diff mode exists for that morning: pull, run, read the changed line.

## Kortix

Kortix is the open-source AI Operating System: agents, skills, company memory and connectors as files in one git repo a team owns, one isolated machine per session, and work that lands as a change request a person merges. Read it, fork it, audit it at [kortix.com](https://kortix.com).
