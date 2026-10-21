# A published sandbox is not an open product

Picture a platform team that has been asked whether it can bring Perplexity Computer in house. Someone forwards the SPACE announcement from 15 October 2026, notes that the sandbox now has a [public repository](https://www.perplexity.ai/hub/blog/open-sourcing-space), and asks for an opinion by Friday. The honest answer takes a page, because the release is real, the repository is real, and the product is still not something the team can run.

## What the published sandbox is worth

SPACE is the platform where Computer's sessions execute. Perplexity says it replaced a commercial sandbox vendor in July 2026 and has run every Computer session since, which makes this the rare publication a reviewer can treat as production evidence rather than a sample.

For a team, that buys three things. It can read the code that runs an agent's commands, instead of trusting a diagram in a security questionnaire. It can test its own isolation requirements against the same implementation the vendor ships. And it can put the platform on its own infrastructure if it has the capacity, which turns a hosting question into an engineering one.

Those are the gains a published execution layer always brings. They are also where the gains stop.

## What the team still cannot do

The team cannot change what the product plans. Computer turns a goal into subtasks and hands them to sub-agents inside [Perplexity's product](https://www.perplexity.ai/help-center/en/articles/13837784-what-is-computer), and that planner has no published source. Run the sandbox on your own hardware and the work sent into it still arrives from a planner you cannot read, adjust or replace.

The team cannot choose the routing. Perplexity routes each query across models it picks, and the router is outside the release. A team that self-hosts a sandbox and keeps the product above it has bought control of the machine and none of the scheduling.

The team cannot replace the connectors. Gmail, Outlook, GitHub, Linear, Slack and Notion are reached through connections Perplexity manages, and neither the catalogue nor its authorization is published. For most teams this is the layer that matters most in a review, because it is where a subscriber's data is reachable and where the credentials live.

The team cannot take the configuration with it. The Agent API accepts versioned Profiles and Skills and lets a subscriber reuse them across applications, but those [definitions execute inside Perplexity's cloud](https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents). Reuse is a real convenience. It is not an export.

Put together, the four gaps describe the same thing. The published layer does what it is told. The unpublished layers decide, and a team that owns only the first one has bought a faster machine with the same supplier.

## The local-hardware case is the trap

Portable Computer looks like the answer and is not. It runs the orchestrator, the planner, the scheduler and the sandbox on a subscriber's own NVIDIA GPU, either a DGX Spark or a 24 GB RTX card on Windows, Ubuntu or DGX OS, and it [still requires a Pro or Max plan](https://www.perplexity.ai/help-center/en/articles/20260915-what-is-portable-computer).

Two facts sit side by side in that sentence, and buyers routinely keep only one. The computation moves onto hardware the team owns. The code does not move into a repository the team can read, and the subscription does not go away. A DGX Spark in a rack is a capital expense attached to a closed product, which is a different proposition from an open stack on the same box.

## What would have to change for the answer to change

Two conditions would move a team from "we can host the execution layer" to "we can run the product".

The first is publication of the deciding layer. That means the agent and planner, and the router, each with a source URL and a date, the way the sandbox has one now. A team could then read how a goal becomes subtasks, see which model is chosen for which query, and fork the behaviour when its own policy differs. Until that exists, every conversation about customising Computer ends at the same wall.

The second is a documented boundary the team can rely on. Even without published source, a vendor can state what runs where, which credentials the platform holds, what leaves the tenant, and what a subscriber keeps on exit, in language specific enough to survive a review. That statement is worth less than source, and considerably more than a marketing page, because a team can hold a vendor to a written boundary.

A team should ask for both and accept either as progress. What it should not accept is a headline that names one layer and implies the rest.

## Keeping the answer current

The boundary moves. A router can be published, a repository can be archived, a help centre page can be rewritten, and a plan requirement can change with a release note. Any of those events changes the answer for a buyer, and none of them announces itself to a team that checked once.

The audit in this repository is built for that rhythm. Each layer carries a source URL and a checked date, the run records what each URL returned, and the diff mode compares a fresh run with a snapshot you kept. A change in the boundary appears as a changed line rather than as a surprise in a renewal meeting.

Kortix is the open-source AI Operating System. Run it on Kortix Cloud, in your VPC, or on your own on-prem network. Self-host is free. The deciding layers sit in the repository the team holds, at [kortix.com](https://kortix.com).
