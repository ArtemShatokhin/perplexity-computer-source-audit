# How to verify an open-source claim about any AI product

A vendor page says "open source". A comparison post says "closed". Neither sentence tells a buyer whether the product can be run, whether the part that makes decisions can be read, or whether the answer will still hold next quarter. Four checks settle the question, and a buyer can run all four in an afternoon without reading code.

The method below is the one this repository automates for Perplexity Computer, and it works on any vendor that ships an agent product, because it asks for artifacts and dates rather than opinions.

## Step 1: find the artifact

Start with a URL, not an adjective. An open-source claim is a claim about a specific thing that exists: a repository, a published package, a downloadable build. Ask which one, and open it.

A claim with no artifact behind it gives a buyer nothing to check, and it should not survive into a procurement note. When a vendor publishes several things, list them separately, because they usually cover different parts of the product.

Perplexity's SPACE announcement names its artifact in the first lines: a repository at [github.com/perplexityai/SPACE](https://www.perplexity.ai/hub/blog/open-sourcing-space), published on 15 October 2026. That is a usable answer to step one.

## Step 2: find the licence file, or find that there is none

Open the repository root and look for the file that states what the publication permits. Read what the vendor's own post says next to it. If the post uses a narrow phrase such as "publicly released" and the repository carries no licence file, the honest description is the vendor's phrase, not the stronger one a headline prefers.

This is where summaries go wrong in both directions: naming terms the vendor never stated, or calling a publication closed without opening the file. A buyer needs one of two outcomes, a stated permission or a note that it is unstated.

The audit in this repository takes no position on terms at all. It records that a layer is published and links the page that says so, because a licence question is a lawyer's question and a publication question is a buyer's.

## Step 3: check that the artifact is the thing that decides

This is the step almost everyone skips, and it is the one that changes conclusions.

A published artifact can sit at the edge of a product and still be described as the product being open. The test is whether that code makes the decisions a buyer cares about: what work gets done, which model answers, what the system reaches, where the data goes.

Perplexity Computer is six layers arranged in a stack. SPACE is the sandbox, the layer that executes commands inside a session. The agent that plans a goal into subtasks and hands them to sub-agents is described in the [product help centre](https://www.perplexity.ai/help-center/en/articles/13837784-what-is-computer) and not published. The router that picks a model per query is outside the release. The managed connectors into Gmail, Outlook, GitHub, Linear, Slack and Notion are not published either. One layer of six is a real publication and a partial answer.

Portable Computer makes the same point in a different shape. It runs the orchestrator, the planner, the scheduler and the sandbox on a subscriber's own NVIDIA GPU, a DGX Spark or a 24 GB RTX card on Windows, Ubuntu or DGX OS, and it [still requires a Pro or Max plan](https://www.perplexity.ai/help-center/en/articles/20260915-what-is-portable-computer). Code on hardware you own is not code you can read.

## Step 4: check the date

Every claim about publication expires. Vendors publish, rename, merge and withdraw, and a page that answered in July can be wrong by October.

Look for a date in two places: the vendor's post and your own check. The useful sentence is "on this date, this URL said this". A repository that exists today may be archived next year.

The audit stores a checked date per layer and a `generated_at` stamp per snapshot, then compares snapshots so the date becomes visible instead of implied. Running `python3 audit.py --diff snapshot-2026-10-21.json` prints one line per layer and reports a flipped publication state, a moved source URL or a source that stopped answering. That is the difference between a claim and a measurement.

## The four steps applied once

The method run end to end on 21 October 2026 produces six rows. One layer published on 15 October 2026 with a repository and a vendor statement. Four layers unpublished, each with a URL that describes the layer without publishing it. One layer partly published: the Agent API accepts versioned Profiles and Skills and reuses them across applications, while those [definitions execute in Perplexity's cloud](https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents).

The conclusion that survives all four steps is narrower than either headline. Perplexity published the layer where Computer's code executes, in the platform it says replaced its commercial sandbox vendor in July 2026 and has run every Computer session since. It did not publish the layers that decide what runs, which model answers, or which apps the product reaches. "Open source now" holds for one layer and fails for five. "Fully closed" now fails for one and holds for five.

## Where the method stops

Four checks answer a publication question. They do not answer whether the published code matches the binary in production, or what the publication permits. They also do not measure quality, which is a separate judgement about a layer either way.

What the checks give a buyer is a habit. Ask for the URL. Ask which layer it covers. Ask when it was last true. A vendor that answers all three is easy to work with, and a vendor that answers none has told you something useful too.

Kortix is the open-source AI Operating System. One isolated sandbox per session. Each session has its own isolated machine and branch, and session work reaches `main` through a change request a person merges. The layers that decide are open to read at [kortix.com](https://kortix.com).
