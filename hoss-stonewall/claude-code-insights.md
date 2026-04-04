---
description: Usage analysis, friction map, and operating upgrades from 77 sessions.
---

# 📈 Claude Code Insights

> A two-week audit of how QB1 uses Claude Code across legal ops, file organization, codex maintenance, and document production.

<a href="../" class="button primary" data-icon="house">Back to the landing page</a> <a href="/broken/pages/Gr7hrx2cO9AmzbzjcLXn" class="button secondary" data-icon="book">Open deep reference</a>

### Snapshot

{% columns %}
{% column %}
* **Messages:** 1,175
* **Sessions:** 77 active, 106 total
* **Usage window:** 2026-03-20 to 2026-04-02
* **Total usage:** 84 hours
{% endcolumn %}

{% column %}
* **Files touched:** 193
* **Lines changed:** +13,926 / -649
* **Days active:** 12
* **Messages per day:** 97.9
{% endcolumn %}
{% endcolumns %}

{% hint style="success" %}
**What is working**

You built a real legal knowledge system across Notion, OneDrive, GitHub, and local files.

You use Claude Code as a production tool, not a toy.

You consistently push large tasks to completion, including 1,500+ file reorganizations, multi-round legal deliverables, and a 30K+ word advocacy book.
{% endhint %}

{% hint style="warning" %}
**What is costing time**

First-pass factual misses keep forcing correction loops.

Cold starts, MCP reconnects, and failed Chrome integration attempts eat too many sessions.

Parallel file work sometimes creates overwrite risk instead of speed.
{% endhint %}

{% hint style="info" %}
**Fastest wins**

Build one bootstrap skill that loads state, conventions, blockers, and current tasks.

Add validation hooks for billing rules, naming conventions, and packaging checks before output is shown.
{% endhint %}

### At a glance

#### Core pattern

You are a power user running marathon sessions.

Your workflow is operations-heavy, document-heavy, and file-heavy.

This is not standard software engineering usage.

This is legal practice management, corpus maintenance, and deliverable production at scale.

#### Key reading

* You use Claude Code as an always-on legal operations platform.
* You work through iterative correction, not pristine up-front specs.
* You aggressively parallelize when volume spikes.
* You catch factual drift and force the model back onto the rails.
* You keep pushing big jobs until they land.

### What you work on

#### Legal knowledge base and codex management

\~18 sessions.

You maintain and upgrade the Stonewall Brain across multiple versions.

The work includes corpus classification, cross-referencing across repo, Notion, and OneDrive, deduplication of 400+ files, factual correction, and QC sweeps.

#### Legal billing and case documentation

\~12 sessions.

You produce billing CSVs for FileVine import, settlement posture reports across 8 UPS matters, client-facing summaries, and case-lookup workflows.

#### File organization and OneDrive sync

\~12 sessions.

You run major reorganizations across local files, repos, and OneDrive, including 1,500+ file sorts, flattening, duplicate removal, and sync repair.

#### Long-form writing and narrative projects

\~8 sessions.

This includes a 30K+ word advocacy book, philosophical chapters, narrative chronologies, and markdown-to-PDF conversion runs.

#### Environment setup and browser automation

\~10 sessions.

This is the least productive cluster.

Chrome browser automation repeatedly failed and blocked validation workflows.

### What you wanted most

* **File organization:** 8
* **Setup / configuration:** 7
* **How-to questions:** 7
* **Git operations:** 6
* **File packaging:** 5
* **Browser automation:** 5

### How you use Claude Code

#### Top tools used

* **Bash:** 1,357
* **Read:** 509
* **Agent:** 305
* **Edit:** 239
* **OneDrive MCP layer:** 172
* **Write:** 132

#### Languages

* **Markdown:** 598
* **JSON:** 39
* **Python:** 18
* **Shell:** 18
* **JavaScript:** 3
* **CSS:** 1

#### Session types

* **Multi-task:** 37
* **Single-task:** 18
* **Iterative refinement:** 17
* **Quick question:** 3
* **Exploration:** 2

#### Operating profile

You rely on shell, file inspection, and broad corpus reads more than code generation.

Markdown dominance confirms the pattern.

This is documentation, synthesis, QC, and structured legal work.

Not app development.

### What stands out

#### Impressive things you did

* Built a custom legal knowledge system with real QC discipline.
* Cross-referenced case materials across Notion, OneDrive, GitHub, and local files.
* Orchestrated large-scale file sorting and deduplication tasks.
* Produced polished client-facing deliverables with repeated tightening.
* Used Claude Code for both tactical legal work and archive-scale writing.

#### What helped most

* **Multi-file changes:** 37
* **Proactive help:** 12
* **Good explanations:** 9
* **Fast / accurate search:** 6
* **Good debugging:** 5
* **Correct code edits:** 1

#### Outcomes

* **Fully achieved:** 18
* **Mostly achieved:** 29
* **Partially achieved:** 17
* **Not achieved:** 7
* **Unclear:** 6

### Friction map

{% columns %}
{% column %}
**Primary friction types**

* **Wrong approach:** 42
* **Misunderstood requests:** 29
* **Buggy output:** 28
* **Tool failure:** 11
* **User rejected action:** 8
* **Excessive changes:** 4
{% endcolumn %}

{% column %}
**Inferred satisfaction**

* **Likely satisfied:** 127
* **Satisfied:** 28
* **Happy:** 7
* **Dissatisfied:** 35
* **Frustrated:** 9
{% endcolumn %}
{% endcolumns %}

#### Recurring failure modes

**Browser and MCP failures**

Chrome MCP integration repeatedly failed.

At least 4 separate sessions were spent retrying the same broken browser path.

This produced full-session waste and unfinished verification work.

**Factual drift on first pass**

Names, dates, billing conventions, and source details were often wrong on first draft.

That drove revision loops like V6 -> V7 -> V8 when the rules should have been stable from the start.

**Non-start sessions**

At least 7 sessions ended without real work.

They were consumed by effort toggles, reconnects, skill loads, or resume confusion.

**Parallel overwrite risk**

You use sub-agents heavily.

That helps on read-only work.

It backfires when multiple agents touch overlapping files.

### Behavior signals

#### Response timing

* **Median response time:** 56.9s
* **Average response time:** 178.1s

#### Multi-clauding

* **Overlap events:** 27
* **Sessions involved:** 33
* **Messages in overlapping sessions:** 16%

You often run parallel sessions.

That supports throughput, but also increases context drift risk.

### Existing features to try

#### Suggested CLAUDE.md additions

<details>

<summary>Browser automation rule</summary>

```md
## Browser Automation
Chrome MCP integration is unreliable on this system. Do NOT attempt Chrome browser automation or MCP chrome extensions. If browser verification is needed, suggest the user do it manually or find an alternative approach. Never retry a failed Chrome MCP connection more than once.
```

Chrome/browser MCP failed across 5+ sessions with repeated futile retries.

</details>

<details>

<summary>Billing and legal document rules</summary>

```md
## Billing & Legal Document Rules
- Never bill on weekends unless explicitly instructed
- Always use FULL names (first + last) in billing entries and legal documents, never last-name-only
- Do not include internal staff names (e.g., ATS staff) in client-facing billing
- Cross-check all court jurisdictions, opposing counsel names, and dates against source documents before finalizing
```

These errors triggered repeated correction loops.

</details>

<details>

<summary>File operations rules</summary>

```md
## File Operations
- Before reorganizing or moving files, READ file contents to determine correct classification — do not rely on filename alone
- Never delete files until the reorganized copy is verified
- When creating zip files, use forward slashes in paths and flatten structure to avoid OS compatibility issues
- Always commit to the correct branch — verify with `git branch` before committing
```

These rules address misclassification, loss risk, broken zip paths, and wrong-branch commits.

</details>

<details>

<summary>Parallel agents rules</summary>

```md
## Parallel Agents
- When spawning sub-agents, ensure they do NOT edit the same files as other agents or the main thread
- Limit parallel agent spawning — do not spawn excessive agents; prefer sequential work for file modifications
- After parallel agent work completes, verify no overwrites occurred before moving on
```

This addresses the repeated overwrite problem.

</details>

<details>

<summary>Notion integration rules</summary>

```md
## Notion Integration
- When user says 'export from Outlook,' do NOT query Notion — export directly from Outlook
- Verify date field formats match Notion's expected input before pushing updates
```

This addresses source confusion and date-format bugs.

</details>

#### Custom skill to add next

```bash
mkdir -p .claude/skills/billing && cat > .claude/skills/billing/SKILL.md << 'EOF'
# Billing Entry Generator
## Rules
- Use FULL names (first + last), never last-name-only
- Never bill on weekends unless explicitly told to
- Do not include internal ATS staff names
- Format: Date | Hours | Description
- Cross-check all names against case files before output
- Output as CSV compatible with FileVine import
EOF
```

Why this matters:

Your billing workflow went through 3+ revision cycles repeatedly.

One dedicated skill would eliminate the same corrections being rediscovered every session.

#### Hooks

```json
{
  "hooks": {
    "postToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "if [[ \"$CC_FILE\" == *.zip ]]; then python -c \"import zipfile; zipfile.ZipFile('$CC_FILE').testzip() or print('ZIP OK')\"; fi"
      }
    ]
  }
}
```

Why this matters:

This catches broken zip output before it becomes downstream pain.

#### Headless mode

```bash
claude -p "Run a full repo QC: check for duplicate files, verify manifest.json matches actual files, ensure no files have Windows-incompatible path characters. Output a report to QC_REPORT.md" --allowedTools "Read,Bash,Glob,Write"
```

Why this matters:

Recurring QC sweeps should not require a fresh interactive session every time.

### New usage patterns

#### Stop retrying broken integrations

When Chrome MCP fails once, abandon it.

Use direct APIs, CLI tools, or manual browser verification instead.

```
The Chrome MCP extension doesn't work on my system. Instead of browser automation, help me verify this data by: (1) telling me exactly what to check manually, (2) giving me the URLs to visit, and (3) I'll paste back what I see.
```

#### Front-load hard requirements

Put constraints first.

Make the system build a checklist before generating output.

```
Before you start, here are the hard requirements: [list rules]. Generate a checklist from these requirements, then produce the output, then self-verify against the checklist before showing me.
```

#### Use sequential agents for file-heavy work

Reserve parallelism for read-only exploration.

Use sequential execution for file mutations.

```
Reorganize these files SEQUENTIALLY — do not spawn parallel agents for file moves or edits. Only use parallel agents for read-only tasks like searching or classifying. Process one folder at a time and verify before moving to the next.
```

### On the horizon

#### Self-correcting parallel agent file organization

The model should build a manifest first.

Every agent should read the manifest before moving a file.

Conflicts should stop the run, not create silent overwrites.

```
I need you to reorganize files in [SOURCE_DIR] into case folders under [DEST_DIR]. Before starting: 1) Scan ALL files and build a manifest.json mapping each file to its proposed destination based on CONTENT (not just filename). 2) Show me the manifest for approval. 3) After approval, spawn parallel agents BUT each agent must: a) read manifest.json before each move, b) write a lock entry before moving, c) verify the file landed correctly after moving, d) log completion to reorganization_log.json. 4) After all moves, run a verification agent that confirms every file in the manifest exists at its destination and no orphans remain. If any agent encounters a conflict, STOP and report rather than overwriting.
```

#### Iterative document generation against quality gates

Generate.

Audit.

Fix.

Re-audit.

Only then present the output.

```
Generate [DOCUMENT_TYPE] for [CASE/PERIOD]. Before showing me ANY output, run this autonomous quality loop: 1) Read CONVENTIONS.md and all referenced case files for ground truth. 2) Generate the document. 3) Self-audit by checking: no last-name-only references (use full names), no weekend dates for billing, all case numbers match canonical sources, all dollar amounts cross-referenced against source docs, tone matches [formal/client-facing/internal]. 4) Fix every violation found. 5) Re-audit. Repeat steps 3-5 up to 3 times. 6) Present the final version WITH an audit report showing what you caught and fixed in each pass. If any fact can't be verified from available files, flag it explicitly rather than guessing.
```

#### Persistent session context via skill bootstrap

One bootstrap layer should load state, conventions, friction history, and blockers on session start.

That cuts non-start sessions and stops known-bad retries.

```
Help me build a session-bootstrap system. Create these files: 1) SESSION_STATE.json — tracks: current active tasks, last session outcome, pending items, known blockers (like Chrome MCP not working). 2) CONVENTIONS.md — captures all my document formatting rules, naming conventions, billing rules (no weekends), and file organization preferences. 3) FRICTION_LOG.md — records approaches that failed so you never retry them (e.g., Chrome MCP extension, wrong branch commits). 4) Update my session-resume skill to: load all 3 files first, print a 5-line status brief, and ASK before attempting any approach listed in the friction log. 5) Add a session-close skill that auto-updates SESSION_STATE.json with what was accomplished, what's pending, and any new friction discovered. Test by running session-resume now and showing me the brief.
```

### Sharpest single quote

{% hint style="warning" %}
**Observed failure mode**

"Lawyer kept pasting the 'resume session' command directly into the Claude chat instead of the terminal, failing over and over."

That is not a character flaw.

It is a bootstrap and workflow design problem.

The fix is stronger session ergonomics.
{% endhint %}

### Bottom line

The report shows a serious operator using Claude Code for real work at scale.

The ceiling is already high.

The drag comes from cold starts, browser dead ends, factual first-pass misses, and unguarded parallel edits.

The shortest path forward is simple:

1. Bootstrap state automatically.
2. Encode conventions once.
3. Validate before presenting.
4. Stop retrying broken browser paths.
5. Use sequential execution for file mutations.
