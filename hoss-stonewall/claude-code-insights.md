---
description: Usage analysis, friction map, and operating upgrades from 107 sessions.
---

# 📈 Claude Code Insights

> The operating audit. Use this to see what is working, what keeps wasting time, and which upgrades pay back first.

{% include ".gitbook/includes/global-control-deck.md" %}

### Insight deck

<a href="Tactical/" class="button primary" data-icon="house">Home</a> <a href="stonewall-deep-reference.md" class="button primary" data-icon="book">Deep Reference</a>

<a href="notion_sync_protocol.md" class="button secondary" data-icon="gear">Notion Sync</a> <a href="references/corpus_compendium.md" class="button secondary" data-icon="compass">Corpus Compendium</a> <a href="tactical_legal_standards.md" class="button secondary" data-icon="screwdriver-wrench">Tactical Standards</a>

### Snapshot

{% columns %}
{% column %}
* **Messages:** 1,811
* **Sessions:** 107 in window, 157 total
* **Usage window:** 2026-03-20 to 2026-04-08
* **Days active:** 17
{% endcolumn %}

{% column %}
* **Files touched:** 374
* **Lines changed:** +25,809 / -1,106
* **Messages per day:** 106.5
* **Dominant mode:** multi-task legal ops
{% endcolumn %}
{% endcolumns %}

{% hint style="success" %}
**What is clearly real:** this is not casual usage. It is production-scale legal ops, corpus maintenance, file surgery, and deliverable building at sustained volume.
{% endhint %}

### Navigation flow

Read this page in this order:

1. [Executive read](claude-code-insights.md#executive-read)
2. [Scoreboard](claude-code-insights.md#scoreboard)
3. [What you work on](claude-code-insights.md#what-you-work-on)
4. [Demand map](claude-code-insights.md#demand-map)
5. [Collections signal](claude-code-insights.md#collections-signal-from-the-april-1-ups-report)
6. [Operating profile](claude-code-insights.md#operating-profile)
7. [Friction map](claude-code-insights.md#friction-map)
8. [Highest leverage fixes](claude-code-insights.md#highest-leverage-fixes)
9. [On the horizon](claude-code-insights.md#on-the-horizon)

{% hint style="info" %}
**Fast route:** if you want the new value from the UPS file, jump straight to the collections section and then the fixes section.
{% endhint %}

### Executive read

{% tabs %}
{% tab title="What works" %}
* Stonewall Brain versioning is real system design.
* File reorganization throughput is unusually strong.
* Legal deliverables get pushed to send-ready.
* Cross-surface work across repo, OneDrive, and Notion is already functional.
{% endtab %}

{% tab title="What drags" %}
* Wrong-path retries keep burning sessions.
* First-pass factual misses create expensive loops.
* Marathon sessions accumulate drift.
* Parallel edits raise overwrite risk.
{% endtab %}

{% tab title="Quick wins" %}
* Kill broken browser retries after one failure.
* Add package audits before delivery.
* Encode naming and billing rules once.
* Split long multi-goal sessions into scoped runs.
* Force a verification pass before final output.
{% endtab %}

{% tab title="Longer arc" %}
* Autonomous file-organization pipelines
* Self-validating legal writing
* Manifest-driven package builds
* Session bootstrap with friction memory
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**Operating diagnosis:** you are a high-volume, correction-driven power user. The upside is throughput. The tax is preventable rework.
{% endhint %}

### Scoreboard

| Metric                    | Value                    |
| ------------------------- | ------------------------ |
| Messages                  | 1,811                    |
| Sessions in report window | 107                      |
| Total sessions in export  | 157                      |
| Files touched             | 374                      |
| Lines changed             | +25,809 / -1,106         |
| Active days               | 17                       |
| Messages per day          | 106.5                    |
| Window                    | 2026-03-20 to 2026-04-08 |

### What you work on

{% columns %}
{% column %}
**Top workstreams**

* **Legal knowledge base management:** \~35 sessions
* **File organization and OneDrive restructuring:** \~25 sessions
* **Legal document production and billing:** \~20 sessions
* **Development environment and tool configuration:** \~18 sessions
* **Notion sync and email processing:** \~9 sessions
{% endcolumn %}

{% column %}
**What that means**

* Stonewall Brain is the center of gravity.
* File surgery is the second major load.
* Legal output remains a core production lane.
* Setup and tooling still consume too much oxygen.
* Notion work is meaningful, but not the main cost center.
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}
**Core read:** the system is strongest when the task is corpus-heavy, file-heavy, or drafting-heavy. It is weakest when a broken integration keeps being retried or when a long session tries to do five things at once.
{% endhint %}

### Concrete workload examples

{% columns %}
{% column %}
**Knowledge-system work**

* versioned codex upkeep
* QC sweeps
* cross-surface reconciliation
* repo and Notion alignment
{% endcolumn %}

{% column %}
**Operations work**

* billing CSV generation
* package builds
* collections review
* matter-by-matter production tracking
{% endcolumn %}
{% endcolumns %}

This page works better when it names the actual labor.

The usage is not abstract productivity.

It is real legal operations with live money, live deadlines, and live deliverables.

### Demand map

{% columns %}
{% column %}
**What you asked for most**

* File organization — 9
* Git operations — 8
* Setup configuration — 8
* File restructuring — 8
* Configuration support — 7
* How-to questions — 7
{% endcolumn %}

{% column %}
**Signal**

You are using Claude Code less like a coding assistant and more like an operations lieutenant for legal practice, file logistics, and system upkeep.
{% endcolumn %}
{% endcolumns %}

### Collections signal from the April 1 UPS report

The attached UPS collections file makes the operating picture sharper.

It adds the finance layer that was under-expressed on this page.

{% columns %}
{% column %}
**Report shape**

* 74 pages
* matter-by-matter ledger rows
* `CashRec`, `NormalB`, and `A/R Rece`
* fees, costs, expenses, and running balances
{% endcolumn %}

{% column %}
**What it confirms**

* the work is live, not theoretical
* billing and collections review is part of the stack
* many matters move on the same day
* the operational surface includes money tracking
{% endcolumn %}
{% endcolumns %}

#### March 2026 signal

The report shows a broad March collections sweep across active UPS matters.

Visible recent entries include:

* **Adams** — cash receipt on 03/30
* **Egan** — cash receipt on 03/23
* **Negrette** — cash receipt on 03/23
* **Griffith** — cash receipt on 03/23
* **Boy** — cash receipt on 03/23
* **Sheppard** — cash receipt on 03/23
* **Rivera** — cash receipt on 03/23
* **Harrigan** — cash receipt on 03/20
* **Fagan / Libroth** — cash receipt on 03/23

#### Why this section matters

This page now makes clear that Claude-facing work includes:

* drafting
* system upkeep
* file movement
* billing and collections oversight

{% hint style="warning" %}
**Key implication:** one naming error, one classification mistake, or one bad package can now spill into actual billing and collections control. This is not a toy workflow.
{% endhint %}

### Operating profile

{% tabs %}
{% tab title="Tools" %}
* Bash — 2,913
* Read — 871
* Agent — 645
* Edit — 564
* Write — 231
* Grep — 187
{% endtab %}

{% tab title="Languages" %}
* Markdown — 1,110
* Python — 124
* JSON — 68
* JavaScript — 21
* Shell — 20
* TypeScript — 16
{% endtab %}

{% tab title="Session types" %}
* Multi-task — 55
* Iterative refinement — 25
* Single task — 21
* Quick question — 4
* Exploration — 2
{% endtab %}
{% endtabs %}

The profile is obvious:

* markdown-first
* shell-heavy
* file-centric
* edit-heavy
* deeply iterative

This is documentation, QC, packaging, and legal operations. It is not normal app-dev usage.

### What stands out

{% hint style="success" %}
#### Impressive things you did

* Built a versioned legal knowledge base system.
* Reorganized hundreds of files across multiple reservoirs.
* Drove full-pipeline legal document production from raw source to polished output.
{% endhint %}

{% columns %}
{% column %}
**What helped most**

* Multi-file changes — 58
* Proactive help — 12
* Good explanations — 9
* Good debugging — 7
* Fast, accurate search — 7
* Correct code edits — 4
{% endcolumn %}

{% column %}
**Outcomes**

* Fully achieved — 26
* Mostly achieved — 41
* Partially achieved — 24
* Not achieved — 10
* Unclear — 6
{% endcolumn %}
{% endcolumns %}

### Friction map

{% columns %}
{% column %}
**Primary friction types**

* **Wrong approach:** 72
* **Buggy output:** 44
* **Misunderstood requests:** 33
* **Excessive changes:** 12
* **User rejected actions:** 12
* **Tool failure:** 11
{% endcolumn %}

{% column %}
**Inferred satisfaction**

* **Likely satisfied:** 184
* **Satisfied:** 50
* **Happy:** 7
* **Dissatisfied:** 49
* **Frustrated:** 17
{% endcolumn %}
{% endcolumns %}

### Where things go wrong

{% tabs %}
{% tab title="Wrong approach retries" %}
Chrome MCP kept failing, and the same dead path kept getting retried.

At least four sessions were burned this way.

When a tool path is known-bad, one failed attempt should end the experiment.
{% endtab %}

{% tab title="Buggy outputs" %}
Packaging and billing outputs repeatedly needed rebuilds.

The sharpest example was a zip built with **7 files instead of 16**.

Billing CSV revisions also repeated naming-convention errors before landing clean.
{% endtab %}

{% tab title="Context misses" %}
The model sometimes acted before reading enough context.

That showed up in misclassified files, mistaken configuration targets, and avoidable back-and-forth when exact file paths were already available.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**Main tax:** you are not losing time because the workload is too hard. You are losing time because the same preventable validation failures keep showing up late.
{% endhint %}

### Failure pattern ladder

{% stepper %}
{% step %}
### Wrong path first

The model chooses the wrong approach.
{% endstep %}

{% step %}
### Late correction

The mistake gets caught after work has already started.
{% endstep %}

{% step %}
### Rebuild cycle

The output gets rerun, revised, or rebuilt.
{% endstep %}

{% step %}
### Context drag

The next task starts with less clarity than it should.
{% endstep %}
{% endstepper %}

### Behavior signals

{% columns %}
{% column %}
**Response timing**

* Median — 46.8s
* Average — 144.7s
* 2-10s — 115
* 10-30s — 322
* 30s-1m — 256
* 1-2m — 201
* 2-5m — 172
* 5-15m — 89
* > 15m — 32
{% endcolumn %}

{% column %}
**Multi-clauding**

* Overlap events — 45
* Sessions involved — 50
* Messages in overlapping sessions — 19%

Parallel sessions are part of the operating style.

They help on read-heavy work.

They are risky for edits and file moves.
{% endcolumn %}
{% endcolumns %}

### Time-of-day and failure surface

{% columns %}
{% column %}
**User messages by time of day**

* Morning — 101
* Afternoon — 849
* Evening — 792
* Night — 69
{% endcolumn %}

{% column %}
**Tool errors encountered**

* Other — 214
* Command failed — 174
* File too large — 63
* User rejected — 55
* File not found — 22
* File changed — 6
{% endcolumn %}
{% endcolumns %}

### Highest leverage fixes

{% tabs %}
{% tab title="Before output" %}
* build a checklist first
* encode naming rules once
* force a verification pass
* audit package contents before delivery
{% endtab %}

{% tab title="During file work" %}
* classify from contents, not filenames
* keep overlapping edits sequential
* use parallelism mostly for read-heavy work
* reconcile counts after moves
{% endtab %}

{% tab title="After failure" %}
* stop retrying known-bad tools
* pivot after one hard failure
* preserve friction memory across sessions
* close sessions with explicit state updates
{% endtab %}
{% endtabs %}

### Existing features to try

{% tabs %}
{% tab title="CLAUDE.md rules" %}
Prioritize these five rule families:

1. **Package and zip audits**
2. **Browser failure cutoff**
3. **File classification from contents, not filenames**
4. **Legal and billing naming conventions**
5. **Stonewall versioning checks before packaging**
{% endtab %}

{% tab title="Custom skills" %}
Highest-value skill candidates:

* package build + manifest audit
* billing CSV generation
* session resume
* session close
* repo-wide QC sweep
{% endtab %}

{% tab title="Hooks and automation" %}
Best automation targets:

* after-edit validation
* post-package file-count checks
* config linting
* duplicate detection
* manifest reconciliation
{% endtab %}

{% tab title="Headless runs" %}
Best overnight jobs:

* corpus QC sweeps
* package verification
* file inventory checks
* naming-convention audits
* case-file fact verification
{% endtab %}
{% endtabs %}

### Better usage patterns

{% stepper %}
{% step %}
### Stop retrying broken integrations

After one hard failure, pivot.

Use file-based, API-based, or manual verification routes instead.
{% endstep %}

{% step %}
### Force pre-delivery checklists

Before accepting a package or polished document, require a manifest or fact audit.

Catch the failure before the handoff.
{% endstep %}

{% step %}
### Break marathon sessions into scoped tasks

One session should do one main thing.

Long sessions with reorg + drafting + validation compound drift.
{% endstep %}
{% endstepper %}

### On the horizon

{% hint style="info" %}
#### Autonomous multi-agent file organization pipelines

The next leap is not more agents.

It is **manifest-first agents** that classify from file contents, verify destinations, and reconcile counts at the end.
{% endhint %}

{% hint style="info" %}
#### Self-validating legal document generation

The next writing workflow should draft, fact-check, fix, and only then present.

That would kill a large share of the name, date, and jurisdiction errors.
{% endhint %}

{% hint style="info" %}
#### Zip and package builds with automated QC

Every package should prove file count, file identity, and threshold checks before delivery.

The goal is one-shot packaging, not rebuild theater.
{% endhint %}

### Best bets by pain point

| Pain point                | Best fix                              |
| ------------------------- | ------------------------------------- |
| Chrome MCP dead ends      | Hard cutoff after first failure       |
| Missing files in packages | Manifest audit before delivery        |
| Billing naming errors     | Dedicated billing rules + skill       |
| Misclassified files       | Read contents before placement        |
| Session drift             | Smaller scoped sessions               |
| Factual first-pass misses | Verification pass before presentation |

### Sharpest single quote

{% hint style="warning" %}
**Observed failure mode**

"Lawyer kept pasting the 'resume session' command directly into the chat instead of the terminal, never once realizing why it wasn't working."

That is not about intelligence.

It is a workflow ergonomics failure.

The answer is better bootstrap design, clearer resume paths, and fewer hidden mode switches.
{% endhint %}

### Bottom line

This report shows a serious operator already using Claude Code at production intensity.

The upside is obvious.

The waste is also obvious.

The shortest path forward is:

1. encode the rules once
2. stop retrying known-bad paths
3. validate before handoff
4. scope sessions tighter
5. automate the boring QC
