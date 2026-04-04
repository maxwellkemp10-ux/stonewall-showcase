---
description: Production-grade legal intelligence for high-volume litigation teams.
icon: scale-balanced
metaLinks:
  alternates:
    - https://app.gitbook.com/s/2gzprIe0ymqfqsequAXB/
---

# Stonewall — Legal Document Intelligence Platform

## Stonewall

Stonewall is a production-grade legal document intelligence platform for high-volume litigation teams.

It turns filings, emails, transcripts, and matter activity into a structured, searchable, auditable operating layer.

It is built for teams that need fast recall, clean chronology, and outputs they can defend.

<a href="docs/ARCHITECTURE.md" class="button primary" data-icon="sitemap">View architecture</a> <a href="SKILL.md" class="button secondary" data-icon="brain">Open skill surface</a> <a href="docs/showcase-repo-handoff.md" class="button secondary" data-icon="shield">Showcase runbook</a>

{% hint style="success" %}
**Fast read**

* **What it is** — a governed legal intelligence layer
* **What it does** — ingests, links, classifies, verifies, and reports
* **Why it matters** — less drift, faster recall, cleaner evidence trails
{% endhint %}

<table data-view="cards"><thead><tr><th>Title</th><th data-card-target data-type="content-ref">Target</th></tr></thead><tbody><tr><td><strong>Architecture</strong><br>System layers, pipeline flow, and core scripts.</td><td><a href="docs/ARCHITECTURE.md">ARCHITECTURE.md</a></td></tr><tr><td><strong>Document skill</strong><br>The analysis protocol for case files, transcripts, and email.</td><td><a href="SKILL.md">SKILL.md</a></td></tr><tr><td><strong>Showcase handoff</strong><br>Public-safe export rules and repo hygiene.</td><td><a href="docs/showcase-repo-handoff.md">showcase-repo-handoff.md</a></td></tr></tbody></table>

***

### Why this exists

Modern litigation generates thousands of emails, filings, depositions, and case events per month.

Stonewall converts that volume into a working record.

Not a demo record.

A usable one.

{% columns %}
{% column %}
#### Built for

* High-volume litigation teams
* Multi-matter case managers
* Document-heavy defense workflows
* Operators who need fast retrieval
{% endcolumn %}

{% column %}
#### Delivers

* Matter-linked email corpus
* AI-assisted tagging
* Date and hold tracking
* QC before publication
{% endcolumn %}
{% endcolumns %}

***

### What Stonewall does

{% tabs %}
{% tab title="Ingest" %}
* Pulls from OneDrive document trees
* Parses Outlook CSV email exports
* Converts raw files into durable markdown derivatives
* Keeps case context attached from the start
{% endtab %}

{% tab title="Structure" %}
* Routes records to the right matter
* Normalizes email and document fields
* Builds searchable text instead of loose files
* Stores live matter state in Notion
{% endtab %}

{% tab title="Verify" %}
* Cross-checks corpus against case data
* Flags broken links, missing fields, and drift
* Preserves source priority over summary
* Produces cleaner downstream work product
{% endtab %}
{% endtabs %}

***

### Operating sequence

{% stepper %}
{% step %}
### Intake

Source files and exports land in controlled paths.

**Result:** raw material enters the system.
{% endstep %}

{% step %}
### Normalize

PDF, DOCX, email, and spreadsheet content becomes structured text.

**Result:** searchable artifacts.
{% endstep %}

{% step %}
### Route

Items connect to the correct matter and live record.

**Result:** context stays attached.
{% endstep %}

{% step %}
### Enrich

AI modules classify, tag, and fill structured gaps.

**Result:** useful metadata without manual drag.
{% endstep %}

{% step %}
### Verify

QC checks the corpus against the operational surface.

**Result:** fewer silent errors.
{% endstep %}

{% step %}
### Publish

Teams get usable matter views, briefs, and reports.

**Result:** decision-ready output.
{% endstep %}
{% endstepper %}

***

### Key capabilities

{% columns %}
{% column %}
#### Core workflow

* Multi-source email ingestion
* OneDrive document ingestion
* Matter-linked storage
* AI document tagging
{% endcolumn %}

{% column %}
#### Operational controls

* Legal hold tracking
* Case date management
* Repo consistency checks
* Daily tactical briefing
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}
**Core rule**

If summary conflicts with source, source wins.
{% endhint %}

***

### Platform layers

| Layer          | Primary role                                       |
| -------------- | -------------------------------------------------- |
| **Source**     | OneDrive files, Outlook exports, live case records |
| **Ingestion**  | Converts raw inputs into durable artifacts         |
| **Processing** | Deduplicates, normalizes, and reshapes content     |
| **Sync**       | Wires documents and email to live matter pages     |
| **AI**         | Tags, classifies, and backfills structured gaps    |
| **QC**         | Detects drift before release                       |

#### Retrieval order

1. **Source artifact**
2. **Matter record**
3. **Email corpus**
4. **Archive derivative**
5. **Synthesis layer**

That order is intentional.

It keeps the record legible under pressure.

***

### Public-safe by design

This page shows the machine.

It does not expose the private record.

{% hint style="warning" %}
**Guardrails**

* No client names
* No claim numbers
* No credentials
* No internal lore
* No surviving private identifiers
{% endhint %}

***

### Current public baseline

<details>

<summary>Open current baseline</summary>

* **Indexed artifacts:** 750+
* **Behavioral patterns:** 176
* **Active matter streams:** 40+
* **Operational views and QA canaries:** 15+
* **Primary modules:** 6
* **Showcase baseline:** v9

</details>

***

### Tech stack

| Surface              | Stack                                    |
| -------------------- | ---------------------------------------- |
| **Language**         | Python 3.11+, Node.js 20+, PowerShell 7+ |
| **AI**               | Anthropic Claude API, OpenAI API         |
| **Case operations**  | Notion API                               |
| **Document storage** | Microsoft OneDrive                       |
| **CI/CD**            | GitHub Actions                           |
| **Packaging**        | `uv`, `npm`                              |

***

### Read next

Choose your path.

<a href="docs/ARCHITECTURE.md" class="button primary" data-icon="arrow-right">Go to architecture</a> <a href="SKILL.md" class="button secondary" data-icon="brain">Open document skill</a> <a href="docs/showcase-repo-handoff.md" class="button secondary" data-icon="shield">Open runbook</a>

***

### Closing line

Stonewall is built for teams that want the record to stay legible under pressure.
