# Stonewall — Legal Document Intelligence Platform

[![GitHub Pages](https://img.shields.io/badge/Live-Showcase-c96b3c?style=for-the-badge)](https://maxwellkemp10-ux.github.io/stonewall-showcase/)
[![Official Brief](https://img.shields.io/badge/Read-Official_Brief-1d1d1d?style=for-the-badge)](https://maxwellkemp10-ux.github.io/stonewall-showcase/official-brief.html)
[![Portal Demo](https://img.shields.io/badge/Open-Portal_Demo-0b57d0?style=for-the-badge)](https://maxwellkemp10-ux.github.io/stonewall-showcase/portal/)
[![GitBook](https://img.shields.io/badge/GitBook-Long--Form_Narrative-3884ff?style=for-the-badge)](https://maxwell-kemp.gitbook.io/stonewall-qb3/stonewall-showcase)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776ab?style=flat-square)](#tech-stack)
[![Node](https://img.shields.io/badge/Node.js-20%2B-5fa04e?style=flat-square)](#tech-stack)
[![Notion API](https://img.shields.io/badge/Notion-API-000000?style=flat-square)](#innovation-stack)
[![Claude](https://img.shields.io/badge/Claude-Workflow_Intelligence-d97757?style=flat-square)](#innovation-stack)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-QC_Automation-2088ff?style=flat-square)](#verification-and-qc)

> Stonewall turns litigation exhaust into a live operating corpus. OneDrive folders, Outlook exports, Notion matters, repo-side validation, and AI-assisted classification all move through one system so a legal team can search, cross-check, brief, and act without losing the thread.

Stonewall is a production-grade legal document intelligence platform built for high-volume civil litigation. It is not a generic filing cabinet and it is not a dashboard pasted on top of a CRM. It is a workflow engine for turning emails, filings, deposition material, medical records, and case events into a searchable, auditable operating surface.

The public repository shows the product logic, the automation architecture, and the delivery surfaces that make the system commercially viable: a flat-file corpus, a Notion operator layer, validation-first automation, tactical briefing workflows, and a static portal that can be deployed instantly.

## Live Surfaces

- [Live showcase](https://maxwellkemp10-ux.github.io/stonewall-showcase/) — the fastest way to understand the platform.
- [Official brief](https://maxwellkemp10-ux.github.io/stonewall-showcase/official-brief.html) — the boardroom-safe narrative version.
- [Portal demo](https://maxwellkemp10-ux.github.io/stonewall-showcase/portal/) — the operator-facing command surface.
- [GitBook edition](https://maxwell-kemp.gitbook.io/stonewall-qb3/stonewall-showcase) — the durable long-form product book.
- [Architecture note](docs/ARCHITECTURE.md) — layer-by-layer technical walkthrough.

## By The Numbers

| Metric | Scale |
| --- | ---: |
| Artifacts cataloged | 1,200+ |
| Active cases represented | 60+ |
| Behavioral patterns indexed | 197 |
| Characters profiled | 120+ |
| Emails processed | 6,000+ |
| Artifact types classified | 23 |

## Why This Platform Hits

- **Flat-file intelligence, not black-box storage.** Stonewall treats the corpus as a governed operating layer instead of burying knowledge inside a database no one can inspect.
- **Notion as the live operator layer.** Matters, dates, holds, and cross-links stay visible to the humans actually running the docket.
- **Workflow-ready, not archive-only.** The same corpus that supports search and reporting also sharpens deposition prep, deadline control, and downstream demand packet readiness.
- **Verification built in.** QC scripts and GitHub Actions keep the front door honest instead of letting bad metadata pile up.
- **Public-facing delivery surfaces.** The product can be shown through GitHub Pages, GitBook, and a static portal without turning the underlying system into a SaaS toy.

## Innovation Stack

### 1. Litigation Corpus As A Searchable Operating Layer

Stonewall is built around the idea that a litigation practice should have a living corpus, not a graveyard of attachments. Documents and email records are converted into structured text, linked to matters, and kept queryable so a team can find what matters fast instead of re-learning the file from scratch every week.

### 2. Notion As The Operator Layer

The Notion stack is not decorative. It is where case posture, legal hold status, date fields, document relations, and email links become legible to the team. `notion_wire_cases.py`, `notion_case_dates.py`, `notion_consolidate_emails.py`, and the repair scripts turn Notion into an execution surface rather than a passive notes app.

### 3. DataGavel Workflow Readiness

Stonewall is designed to prepare the factual substrate that downstream report and damages workflows depend on. When chronology, treatment history, deposition posture, filings, and correspondence are already organized, a DataGavel-style production workflow stops being a scramble and starts becoming a repeatable finishing step.

### 4. Tactical Live Deposition Tailoring

A good deposition outline should move with the file, not lag behind it. Stonewall makes that possible by keeping the recent filings, transcript derivatives, case chronology, and actor-level context in one place so an outline can be adjusted in real time as the theory of the case sharpens.

### 5. Verification-First Automation

Most legal-tech stacks fail because they automate intake and neglect truth maintenance. Stonewall does the opposite. `qc_sweep.mjs`, `repo_sweep.py`, `verify_repo_consistency.py`, and `tactical_brief.py` create a loop where ingestion, sync, and audit are part of one operating rhythm.

### 6. Static Publication Surfaces

The platform can be demonstrated cleanly through GitHub Pages, GitBook, and a static portal because the product has a real architecture under it. That matters commercially. It means the system can be shown, evaluated, and sold without pretending the product is just a slide deck.

## Architecture

```text
OneDrive / Outlook Export
          |
          v
    Ingestion Layer
  ingest_onedrive.py
   parse_emails.ps1
          |
          v
   Processing Layer
email_consolidator.mjs
   email_defuzz.mjs
    email_to_md.py
     docx_to_md.py
          |
          v
    Notion Sync Layer
 notion_wire_cases.py
 notion_wire_batch.py
 notion_case_dates.py
 notion_consolidate_emails.py
          |
          v
   AI Tagging Layer
  email_deep_tag.mjs
 legal_matters_fill.mjs
 legal_hold_backfill.mjs
          |
          v
 Verification + Reporting
     qc_sweep.mjs
 verify_repo_consistency.py
    tactical_brief.py
          |
          v
   Portal / Brief / GitBook
```

## Representative Workflows

### Morning Operating Brief

Start the day with a focused read on deadlines, recent case activity, and backlog:

```bash
python scripts/tactical_brief.py today
```

### OneDrive Ingestion

Walk firm-side document trees, convert documents into usable derivatives, and prepare the archive:

```bash
uv run --with pypdf --with cryptography python scripts/ingest_onedrive.py ingest \
  --root firm --glob "*.pdf" --limit 50
```

### Case Date Wiring

Push litigation dates into the matter registry so the calendar and the corpus stay aligned:

```bash
uv run python scripts/notion_case_dates.py --csv case_dates.csv
```

### QC Sweep

Cross-check the registry against the working corpus before drift becomes operational pain:

```bash
NOTION_TOKEN=ntn_xxx node scripts/qc_sweep.mjs
python scripts/verify_repo_consistency.py
```

## Scripts That Matter Most

| Surface | Scripts |
| --- | --- |
| Ingestion | `ingest_onedrive.py`, `parse_emails.ps1`, `docx_to_md.py`, `transcribe_repo_pdfs.py` |
| Processing | `email_consolidator.mjs`, `email_defuzz.mjs`, `email_to_md.py` |
| Notion sync | `notion_wire_cases.py`, `notion_wire_batch.py`, `notion_case_dates.py`, `notion_consolidate_emails.py` |
| AI fill and tagging | `email_deep_tag.mjs`, `email_audit.mjs`, `legal_matters_fill.mjs`, `legal_hold_backfill.mjs` |
| QC and reporting | `qc_sweep.mjs`, `repo_sweep.py`, `verify_repo_consistency.py`, `tactical_brief.py`, `legal_matters_pdf.py` |

## Verification And QC

Stonewall treats verification as a feature, not a maintenance chore.

- `qc_sweep.mjs` cross-checks the Notion layer against the working corpus.
- `verify_repo_consistency.py` validates catalog and corpus alignment.
- `repo_sweep.py` catches hygiene failures before they compound.
- GitHub Actions can run the checks continuously so drift shows up early.

That is one of the platform's real commercial advantages. A workflow system that cannot prove its own consistency eventually becomes another source of confusion.

## Tech Stack

| Layer | Technology |
| --- | --- |
| Languages | Python 3.11+, Node.js 20+, PowerShell 7+ |
| AI | Anthropic Claude API, OpenAI API |
| Knowledge layer | Notion API |
| Source reservoir | Microsoft OneDrive |
| CI / automation | GitHub Actions |
| Delivery surfaces | GitHub Pages, GitBook, static portal |

## Managed Implementation

Stonewall is structured as a managed implementation for law firms that want a serious litigation intelligence system without building an internal product team.

Implementation can include:

- corpus architecture and folder strategy
- Notion database design and matter wiring
- email ingestion and deduplication rules
- date, hold, and reporting workflows
- AI-assisted tagging and repair loops
- portal and publication surfaces for internal or client-safe visibility

The public repository is the proof surface. The implementation work is the product.

## License

Copyright (c) 2026 Stonewall Legal Intelligence. All rights reserved.  
Provided for evaluation and discussion purposes. For implementation licensing, contact the author.
