---
description: Production-grade legal intelligence for high-volume litigation teams.
icon: scale-balanced
metaLinks:
  alternates:
    - https://app.gitbook.com/s/2gzprIe0ymqfqsequAXB/
---

# Stonewall — Legal Document Intelligence Platform

## Stonewall

Production-grade legal intelligence for high-volume litigation teams.

Stonewall turns filings, email, transcripts, and matter activity into a governed record.

It is built for teams that need fast recall, clean chronology, and outputs they can defend.

***

### I. Abstract

Stonewall is a document intelligence system.

It ingests raw legal material, normalizes it into durable text, routes it to case records, enriches it with AI classification, and verifies the result through repo-based QC.

The point is not novelty.

The point is disciplined retrieval.

#### Current frame

* **Primary sources** — OneDrive documents, Outlook exports, live case records
* **Control surfaces** — Notion databases, Git-backed repo, scripted QC
* **Primary outputs** — timelines, issue ladders, matter summaries, operational briefs
* **Public baseline** — architecture preserved, private matter detail removed

***

### II. Why it works

| Principle                      | What happens                                                   | Why it matters             |
| ------------------------------ | -------------------------------------------------------------- | -------------------------- |
| **Deterministic retrieval**    | Queries resolve through a fixed authority order.               | Less drift. Better recall. |
| **AI-assisted classification** | Documents and emails get structured context fast.              | Less manual sorting.       |
| **Source-traceable synthesis** | Summaries stay tethered to the record.                         | Easier verification.       |
| **Repo-level quality control** | Scripts catch broken links, missing fields, and corpus drift.  | Safer outputs.             |
| **Privacy-first canonization** | Public content keeps the system shape without exposing people. | Showcase-safe by design.   |

***

### III. Operational sequence

| Stage              | Function                                                               | Result                          |
| ------------------ | ---------------------------------------------------------------------- | ------------------------------- |
| **01 — Intake**    | Source files and exports land in controlled paths.                     | Raw material enters the system. |
| **02 — Normalize** | PDF, DOCX, email, and spreadsheet content becomes structured markdown. | Searchable text.                |
| **03 — Route**     | Items connect to the right matter.                                     | Context stays attached.         |
| **04 — Analyze**   | AI modules classify, extract, and summarize.                           | Signal emerges from volume.     |
| **05 — Verify**    | QC catches drift, gaps, and unsupported claims.                        | Confidence rises.               |
| **06 — Publish**   | Teams receive usable records and decision-ready work product.          | Operational output.             |

***

### IV. System composition

| Layer                | Core tools                                                  | Role                                             |
| -------------------- | ----------------------------------------------------------- | ------------------------------------------------ |
| **Source layer**     | OneDrive, Outlook CSV exports                               | Origin of record material                        |
| **Ingestion layer**  | `ingest_onedrive.py`, `parse_emails.ps1`                    | Converts inputs into durable artifacts           |
| **Processing layer** | `email_consolidator.mjs`, `email_to_md.py`, `docx_to_md.py` | Normalizes and deduplicates                      |
| **Sync layer**       | `notion_wire_cases.py`, `notion_case_dates.py`              | Wires documents and email to live matter records |
| **AI layer**         | `email_deep_tag.mjs`, `legal_matters_fill.mjs`              | Classifies and fills structured gaps             |
| **QC layer**         | `qc_sweep.mjs`, `verify_repo_consistency.py`                | Detects drift before release                     |

#### Retrieval order

1. **Source artifact**
2. **Matter record**
3. **Email corpus**
4. **Archive derivative**
5. **Synthesis layer**

That order matters.

If summary conflicts with source, source wins.

***

### V. Operating modes

#### Analytical mode

Use this for interpretation.

* Contradiction mapping
* Posture analysis
* Narrative synthesis
* Pattern extraction

#### Execution mode

Use this for work product.

* Outlines
* Drafts
* Matter routing
* Verified operational outputs

***

### VI. Public-safe showcase

This space keeps the machine.

It removes the private record.

#### Entry points

* [Architecture — Stonewall Legal Document Intelligence Platform](docs/ARCHITECTURE.md)
* [Document Intelligence Skill](SKILL.md)
* [Stonewall Showcase — Repository Handoff Runbook](docs/showcase-repo-handoff.md)

#### Guardrails

* No client names
* No claim numbers
* No credentials
* No private lore
* No internal identifiers that survive sanitization

***

### VII. Working numbers

| Metric                                | Current public baseline |
| ------------------------------------- | ----------------------- |
| **Indexed artifacts**                 | 750+                    |
| **Behavioral patterns**               | 176                     |
| **Active matter streams**             | 40+                     |
| **Operational views and QA canaries** | 15+                     |
| **Primary modules**                   | 6                       |
| **Showcase baseline**                 | v9                      |

***

### VIII. Primary capabilities

* **Multi-source ingestion** — documents and email exports enter through one controlled pipeline
* **Case-linked storage** — records attach to matter pages, not loose folders
* **AI enrichment** — classification and property fill without losing traceability
* **Legal hold tracking** — matters can be backfilled and monitored at scale
* **Batch processing** — larger jobs can move without rate-limit friction
* **CLI operations** — daily brief, repo sweep, and reporting live in scripts
* **Continuous verification** — pushes trigger consistency checks instead of silent drift

***

### IX. Technical baseline

| Surface              | Stack                                    |
| -------------------- | ---------------------------------------- |
| **Language**         | Python 3.11+, Node.js 20+, PowerShell 7+ |
| **AI**               | Anthropic Claude API, OpenAI API         |
| **Case operations**  | Notion API                               |
| **Document storage** | Microsoft OneDrive                       |
| **CI/CD**            | GitHub Actions                           |
| **Packaging**        | `uv`, `npm`                              |

***

### X. Implementation notes

Stonewall is designed as an operating surface, not a demo wrapper.

The repo stores normalized derivatives.

Notion holds the live matter view.

Scripts move data between them.

QC scripts keep those surfaces aligned.

That is the loop.

***

### XI. Read next

If you want the technical stack, read the [architecture page](docs/ARCHITECTURE.md).

If you want the skill surface, read [Document Intelligence Skill](SKILL.md).

If you want the public-safe export rules, read the [showcase handoff runbook](docs/showcase-repo-handoff.md).

***

### XII. Closing line

Stonewall is built for teams that want the record to stay legible under pressure.
