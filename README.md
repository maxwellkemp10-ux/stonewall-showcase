---
icon: scale-balanced
metaLinks:
  alternates:
    - https://app.gitbook.com/s/2gzprIe0ymqfqsequAXB/
---

# Stonewall — Legal Document Intelligence Platform

## Stonewall

Production-grade legal intelligence for high-volume litigation teams.

Stonewall turns email, filings, transcripts, and matter activity into a structured, searchable, auditable operating surface.

{% columns %}
{% column %}
### Why it lands

* **Deterministic retrieval**
* **Audit-safe outputs**
* **AI-assisted classification**
* **Notion-native case operations**
* **Git-backed QC discipline**

<a href="docs/ARCHITECTURE.md" class="button primary" data-icon="sitemap">Explore architecture</a>

<a href="docs/showcase-repo-handoff.md" class="button secondary" data-icon="shield-halved">View showcase guardrails</a>
{% endcolumn %}

{% column %}
### Snapshot

* **750+** indexed artifacts
* **176** behavioral patterns
* **40+** active matter streams
* **6** orchestrated modules
* **15+** operational views and QA canaries
* **v9** public showcase baseline
{% endcolumn %}
{% endcolumns %}

{% hint style="success" %}
This showcase keeps the architecture. It removes private matter detail.
{% endhint %}

***

## Overview

Stonewall is built for firms that need fast recall, disciplined execution, and traceable outputs.

It connects intake, AI tagging, Notion case management, and repo-based QC into one operating loop.

### Showcase entry points

<table data-view="cards"><thead><tr><th>Title</th><th data-card-target data-type="content-ref">Open</th></tr></thead><tbody><tr><td><strong>Architecture</strong><br>See the ingestion, routing, and verification stack.</td><td><a href="docs/ARCHITECTURE.md">ARCHITECTURE.md</a></td></tr><tr><td><strong>Document Intelligence Skill</strong><br>See the productized skill surface and use cases.</td><td><a href="SKILL.md">SKILL.md</a></td></tr><tr><td><strong>Showcase Runbook</strong><br>See how the public-safe narrative stays sanitized.</td><td><a href="docs/showcase-repo-handoff.md">showcase-repo-handoff.md</a></td></tr></tbody></table>

### Innovation map

| Innovation                      | What it does                                                     | Why it matters                             |
| ------------------------------- | ---------------------------------------------------------------- | ------------------------------------------ |
| **Deterministic mode router**   | Separates analytical narration from operational execution.       | Prevents advisory drift.                   |
| **Codex + registry stack**      | Combines identity, chronology, matter state, and pattern memory. | Keeps retrieval governed.                  |
| **Retrieval cascade**           | Resolves queries through a fixed authority order.                | Improves consistency and citation quality. |
| **Privacy-first canonization**  | Rewrites public narrative without exposing people or matters.    | Makes demos safe.                          |
| **QC sweep discipline**         | Reconciles outputs against source-backed artifacts.              | Keeps the corpus audit-ready.              |
| **Multi-surface control plane** | Synchronizes Git, workspace databases, and cloud staging.        | Gives speed without chaos.                 |

### Matter flow

{% stepper %}
{% step %}
### Intake

Email exports and source documents land in controlled intake paths.
{% endstep %}

{% step %}
### Normalize

Raw PDFs, DOCX files, and message content become structured markdown.
{% endstep %}

{% step %}
### Route

Stonewall wires documents and email activity to the right matter.
{% endstep %}

{% step %}
### Analyze

AI modules classify content, extract signal, and surface usable context.
{% endstep %}

{% step %}
### Verify

QC checks catch drift, missing links, and unsourced output before release.
{% endstep %}

{% step %}
### Publish

Legal teams get searchable records, case views, and decision-ready briefs.
{% endstep %}
{% endstepper %}

### Module constellation

| Module                   | Role           | Innovation surface                | Output                         |
| ------------------------ | -------------- | --------------------------------- | ------------------------------ |
| **Core Memory Engine**   | Recall         | Source-traceable retrieval        | Events, documents, posture     |
| **Narrative Lens**       | Interpretation | Executive signal shaping          | Clear synthesis                |
| **Archive Steward**      | Maintenance    | Deduplication and precedence      | Canon quality                  |
| **Cross-Exam Analytics** | Method         | Pattern extraction from testimony | Reusable litigation frameworks |
| **Verbatim Normalizer**  | Input          | Transcript-to-structure pipeline  | Citation-ready text            |
| **Hearing Prep Builder** | Execution      | Verified work-product assembly    | Outlines and issue ladders     |

### Operating modes

{% tabs %}
{% tab title="Analytical mode" %}
Use this mode for explanation, synthesis, and pattern clarity.

* Best for narrative
* Best for contradiction mapping
* Best for posture analysis
{% endtab %}

{% tab title="Execution mode" %}
Use this mode for drafting, routing, and operational outputs.

* Best for outlines
* Best for issue ladders
* Best for witness prep
{% endtab %}
{% endtabs %}

***

## Architecture

```
OneDrive / Email Export
        │
        ▼
  [Ingestion Layer]
  ingest_onedrive.py     ← Converts PDF/DOCX/EML to Markdown derivatives
  parse_emails.ps1       ← Matches Outlook CSV exports to case matters
        │
        ▼
  [Processing Layer]
  email_consolidator.mjs ← Deduplicates and normalizes email records
  email_defuzz.mjs       ← Fuzzy-matches emails to Notion pages
  email_to_md.py         ← Converts raw email data to Markdown
  docx_to_md.py          ← Converts DOCX documents to Markdown
        │
        ▼
  [Notion Sync Layer]
  notion_wire_cases.py          ← Wires email relations to case pages
  notion_wire_batch.py          ← Batch-uploads email records
  notion_case_dates.py          ← Syncs case dates (DOL, discovery, depos)
  notion_backfill_legal_matters.py ← Backfills missing matter properties
  notion_consolidate_emails.py  ← Consolidates datasource into unified DB
        │
        ▼
  [AI Tagging Layer]
  email_deep_tag.mjs     ← AI-powered email classification
  email_audit.mjs        ← Audits and repairs tagging gaps
  legal_matters_fill.mjs ← AI-fills missing Legal Matters properties
  legal_hold_backfill.mjs ← Sets legal hold status on matters
        │
        ▼
  [QC & Reporting Layer]
  qc_sweep.mjs           ← Comprehensive QC cross-check
  repo_sweep.py          ← Repository hygiene checks
  verify_repo_consistency.py ← Validates corpus alignment
  tactical_brief.py      ← CLI daily operating brief
  legal_matters_pdf.py   ← Generates PDF/HTML case management reports
        │
        ▼
  [Notion Databases]
  Legal Matters          ← Primary case registry
  All Email              ← Full email corpus with case relations
  Document Archive       ← Ingested document derivatives
```

***

## Key Capabilities

* **Multi-source email ingestion** — Process Outlook CSV exports from any date range; deduplicate across import batches; match to case matters by subject keywords and claim numbers
* **OneDrive document ingestion** — Walk OneDrive folder trees and convert PDF/DOCX/XLSX/EML to Markdown derivatives with automatic case linkage
* **AI-powered tagging** — Claude and OpenAI classify document type, parties, and relevance; flag missing properties
* **Notion-native case management** — Every case gets a structured Notion page with dates, hold status, email relations, and filing history
* **Legal hold compliance** — Track active/released/not-applicable hold status per matter with automated backfill
* **Batch processing** — Anthropic Batch API integration for high-throughput document processing without rate-limit friction
* **GitHub Actions CI/CD** — QC sweep and consistency checks run on every push; failures surface immediately
* **Tactical CLI** — `python scripts/tactical_brief.py today` for a morning brief: upcoming deadlines, recent case activity, inbox backlog

***

## Tech Stack

| Layer            | Technology                                     |
| ---------------- | ---------------------------------------------- |
| Language         | Python 3.11+, Node.js 20+ (ESM), PowerShell 7+ |
| AI               | Anthropic Claude API, OpenAI API               |
| Case Management  | Notion API                                     |
| Document Storage | Microsoft OneDrive                             |
| CI/CD            | GitHub Actions                                 |
| Email            | Outlook CSV exports                            |
| Packaging        | `uv` (Python), `npm` (Node)                    |

***

## Scripts Overview

### Email Pipeline

| Script                   | Purpose                                                            |
| ------------------------ | ------------------------------------------------------------------ |
| `parse_emails.ps1`       | Parse Outlook CSV exports; match emails to case matters by keyword |
| `email_consolidator.mjs` | Deduplicate and normalize email records across import batches      |
| `email_defuzz.mjs`       | Fuzzy-match email records to existing Notion pages                 |
| `email_bulk_upload.mjs`  | Bulk-upload matched email records to Notion All Email DB           |
| `email_body_push.mjs`    | Push email body text to existing Notion pages                      |
| `email_audit.mjs`        | Audit and repair email tagging, dates, and case relations          |
| `email_deep_tag.mjs`     | AI-powered semantic tagging of email content                       |
| `email_to_md.py`         | Convert raw email data to Markdown format                          |

### Notion Sync

| Script                             | Purpose                                                     |
| ---------------------------------- | ----------------------------------------------------------- |
| `notion_wire_cases.py`             | Wire email-to-case relations in Notion                      |
| `notion_wire_batch.py`             | Batch-process email uploads to Notion                       |
| `notion_case_dates.py`             | Sync case dates (DOL, complaint, discovery, depos) from CSV |
| `notion_consolidate_emails.py`     | Consolidate multiple email datasources into unified DB      |
| `notion_fast_consolidate.py`       | High-throughput consolidation variant                       |
| `notion_fast_dates.py`             | High-throughput date repair across datasources              |
| `notion_date_repair.py`            | Repair malformed date fields in a single datasource         |
| `notion_date_repair_all.py`        | Repair dates across all configured datasources              |
| `notion_email_body_update.py`      | Update email body property across pages                     |
| `notion_backfill_legal_matters.py` | Backfill missing properties on Legal Matters pages          |

### Document Ingestion

| Script                    | Purpose                                                              |
| ------------------------- | -------------------------------------------------------------------- |
| `ingest_onedrive.py`      | Walk OneDrive; convert documents to Markdown; sync to Notion Archive |
| `ingest_onedrive.ps1`     | PowerShell wrapper for `ingest_onedrive.py`                          |
| `docx_to_md.py`           | Standalone DOCX-to-Markdown converter                                |
| `transcribe_repo_pdfs.py` | Extract text from PDFs in the repository                             |

### Legal Matter Tools

| Script                    | Purpose                                              |
| ------------------------- | ---------------------------------------------------- |
| `legal_matters_fill.mjs`  | AI-fill missing properties on Legal Matters pages    |
| `legal_matters_pdf.py`    | Generate PDF/HTML case management report from Notion |
| `legal_hold_backfill.mjs` | Set legal hold status on matters with blank status   |

### QC & Reporting

| Script                       | Purpose                                                         |
| ---------------------------- | --------------------------------------------------------------- |
| `qc_sweep.mjs`               | Cross-check Notion DB against local case index and email corpus |
| `repo_sweep.py`              | Repository hygiene: orphan detection, consistency checks        |
| `verify_repo_consistency.py` | Validate catalog/corpus alignment                               |
| `tactical_brief.py`          | CLI daily operating brief from live corpus                      |
| `repo_data_push.mjs`         | Push repository data to Notion for reporting                    |

### Batch Processing

| Script               | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| `split_batches.ps1`  | Split large JSON payloads into Anthropic Batch API batches |
| `check_output.ps1`   | Inspect batch output distribution                          |
| `run_nap_job.ps1`    | Launch a NAP (Notion Async Processing) job                 |
| `start_nap_job.ps1`  | Start a background NAP job                                 |
| `nap_job_status.ps1` | Check NAP job status                                       |

***

## Getting Started

### Prerequisites

* Python 3.11+ with `uv` package manager
* Node.js 20+
* PowerShell 7+ (Windows/macOS/Linux)
* A Notion workspace with the integration token
* Anthropic API key (for Claude-powered features)
* OpenAI API key (for GPT-powered features)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/stonewall.git
cd stonewall

# Install Python dependencies
uv pip install -r requirements.txt

# Install Node dependencies
npm install
```

### Configuration

Copy `.env.example` to `.env` and populate all required values:

```bash
cp .env.example .env
# Edit .env with your credentials and Notion database IDs
```

**Required environment variables:**

| Variable                  | Description                             |
| ------------------------- | --------------------------------------- |
| `NOTION_TOKEN`            | Notion integration token (`ntn_xxx...`) |
| `NOTION_LEGAL_MATTERS_DB` | Legal Matters database ID               |
| `NOTION_ALL_EMAIL_DB`     | All Email database ID                   |
| `NOTION_ARCHIVE_DB`       | Document Archive database ID            |
| `ANTHROPIC_API_KEY`       | Anthropic Claude API key                |
| `OPENAI_API_KEY`          | OpenAI API key                          |
| `ONEDRIVE_PERSONAL_ROOT`  | Path to personal OneDrive root          |
| `ONEDRIVE_FIRM_ROOT`      | Path to firm OneDrive root              |

See `.env.example` for the complete list.

### Basic Usage

**Refresh case data from Legal Matters:**

```bash
uv run python scripts/ingest_onedrive.py refresh-cases
```

**Ingest documents from OneDrive:**

```bash
uv run --with pypdf --with cryptography python scripts/ingest_onedrive.py ingest --root firm --glob "*.pdf" --limit 50
```

**Sync ingested documents to Notion:**

```bash
uv run python scripts/ingest_onedrive.py sync-notion --limit 50 --workers 4
```

**Parse email exports and match to cases:**

```powershell
.\scripts\parse_emails.ps1
```

**Upload matched emails to Notion:**

```bash
NOTION_TOKEN=ntn_xxx node scripts/email_bulk_upload.mjs --limit 500
```

**Run a QC sweep:**

```bash
NOTION_TOKEN=ntn_xxx node scripts/qc_sweep.mjs
```

**Get daily tactical brief:**

```bash
python scripts/tactical_brief.py today
```

**Generate legal matters report:**

```bash
NOTION_TOKEN=ntn_xxx python scripts/legal_matters_pdf.py --html -o report.html
```

### Running Tests

```bash
# Python test suite
python -m unittest tests.test_ingest_onedrive tests.test_verify_repo_consistency tests.test_tactical_brief

# Node test suite
node --test tests/qb1_tracker_helpers.test.mjs
node --test tests/email_consolidator.test.mjs
```

### CI/CD

GitHub Actions workflows run on every push:

* QC sweep validates Notion data integrity
* Repo consistency check validates corpus alignment
* Static site deployment (if configured)

See `.github/workflows/` for workflow definitions.

***

## Consultancy

This platform is available as a **managed implementation** for law firms. We handle:

* Full environment setup and Notion workspace configuration
* Custom case matching rules calibrated to your docket
* AI tagging models tuned to your practice area
* Ongoing automation maintenance and pipeline extensions
* Training for your legal and administrative team

**Implementation includes:** intake pipeline, email ingestion, document processing, Notion database architecture, QC automation, and reporting dashboards — all production-ready.

_Contact us to discuss an implementation engagement for your firm._

***

## License

Copyright (c) 2026 Stonewall Legal Intelligence. All rights reserved. This software is provided for demonstration and evaluation purposes. For implementation licensing, contact the author.
