# What is actually open in Perplexity Computer

Two people can describe Perplexity Computer in the same week and disagree completely. One says the product is open source now, because Perplexity published a repository in October 2026. The other says it is closed and cannot be self-hosted, because the product is a paid subscription that runs on Perplexity's infrastructure. Neither sentence survives a look at the layers underneath it.

Perplexity Computer is the agent product Perplexity sells to subscribers. It takes a goal, plans the work, hands pieces to sub-agents, executes them somewhere, and reaches into the apps a subscriber has connected. Those are separate jobs done by separate code, and only one was published.

## The release that moved the line

On 15 October 2026 Perplexity published SPACE, the sandbox platform where Computer's sessions execute, at [github.com/perplexityai/SPACE](https://www.perplexity.ai/hub/blog/open-sourcing-space). The same announcement says SPACE replaced a commercial sandbox vendor in July 2026 and has run every Computer session since. That is the reason the release matters: the code a reader can open is the code Perplexity says carries the sessions. It is also the only layer with a repository to open.

## The six layers, and what each one decides

| Layer | Job | Published | Evidence |
| --- | --- | --- | --- |
| Sandbox | Executes each session | Yes, 15 October 2026 | Repository and announcement |
| Agent and planner | Plans a goal, routes subtasks | No | Described in product help only |
| Model router | Picks a model per query | No | Outside the release's scope |
| Connector catalogue | Managed reach into subscriber apps | No | Described, never published |
| Portable Computer | Runs the stack on a local GPU | No | Closed code, plan required |
| Build surface | Profiles and Skills for the API | Partly | Definitions run in Perplexity's cloud |

Each row was checked on 21 October 2026, and the pages cited in this article are its source.

The sandbox holds untrusted code, and it is the layer a security team wants to read, because an agent's commands run there. The agent and planner is the layer that decides what those commands are: Perplexity's help centre describes Computer planning the work and handing it to sub-agents [inside the product](https://www.perplexity.ai/help-center/en/articles/13837784-what-is-computer), and there is no published source for that planning.

The router decides which model answers each query. Perplexity routes a query across models it picks, and the SPACE announcement does not include the router. The connector catalogue decides what Computer can reach: Gmail, Outlook, GitHub, Linear, Slack and Notion arrive through connections Perplexity manages, and neither the catalogue nor its authorization is published. The published layer executes. The unpublished layers choose.

## Why "open source now" overreads one release

The SPACE repository is a fact. The mistake is letting it stand for the product. A reader who sees "open source" in a headline and stops there will assume they can run Computer, which they cannot, because planning, routing and connectivity live elsewhere.

The release is careful about scope. It covers the platform that runs code, and every claim on the page is about execution and isolation. None of them says the agent, the router or the connectors are available.

"Open source" is also easy to write in a headline and hard to qualify in one, since a qualifier has to name the layer, the date and the terms. The nuance drops out at publication, and a reader inherits a claim the vendor never made.

## Why "fully closed" underreads it

The opposite sentence has the same defect. "Perplexity Computer is closed" was accurate until 15 October 2026 and is now wrong about the layer where code runs. A team that wants to know how sessions are isolated, or whether the platform can run outside Perplexity's infrastructure, now has something to read.

That has a use even for a team that will never leave the subscription. Isolation claims are hard to assess from a marketing page, and a repository lets a reviewer check the boundary instead of trusting the diagram, on the layer where a wrong assumption is expensive.

The Portable Computer row is where the two errors meet. Portable Computer runs the orchestrator, the planner, the scheduler and the sandbox on a subscriber's own NVIDIA GPU, either a DGX Spark or a 24 GB RTX card on Windows, Ubuntu or DGX OS, and it [still requires a Pro or Max plan](https://www.perplexity.ai/help-center/en/articles/20260915-what-is-portable-computer). Local hardware is not local source, which is why the row reads "no" in a table about publication and "yes" in a conversation about where computation happens.

The build surface shows a third state that most lists collapse. The Agent API lets a subscriber declare versioned Profiles and Skills and reuse them across applications, but those [definitions execute inside Perplexity's cloud](https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents). Reuse, without the source that would let a team take the definitions elsewhere.

## What a buyer should take from the table

Three questions follow from the rows. Where does the code run, what decides what it does, and what can I keep if I leave. The first now has a public answer. The second and third do not, and reading the sandbox repository will not produce them.

An audit that records those answers with a URL and a date is worth more than an argument about the word "open", because the boundary moves. A vendor can publish the router next quarter or take a repository down, and each event shows up as a changed line when the check is re-run instead of as a new opinion.

Kortix is the open-source AI Operating System: your agents, their skills, your company memory, and every connector in one git repo you own, with the agents working on real cloud computers. The deciding layers are in the repository, not behind it, at [kortix.com](https://kortix.com).
