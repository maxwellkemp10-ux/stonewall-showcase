# Stonewall — Legal Document Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Notion API](https://img.shields.io/badge/Notion-API-000000?logo=notion&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-AI%20Skills-D97757)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)

Stonewall is a production-grade legal document intelligence platform built by a solo litigation attorney to organize a high-volume corpus without relying on a traditional database backend. The system catalogs 1,200+ litigation artifacts, tracks 60+ active matters, indexes 197 behavioral patterns, and turns version-controlled flat files into a portfolio control plane with a static portal, CLI query layer, and AI skill architecture.

The showcase version of Stonewall is intentionally sanitized for public deployment. It demonstrates scale, architecture, and product thinking without exposing client names, case numbers, private correspondence, or privileged work product.

## Snapshot

- 1,200+ artifacts cataloged in a flat-file manifest
- 60+ active cases represented in the public dataset
- 197 behavioral patterns indexed and cross-referenced
- 170+ character profiles represented through role-based aliases
- 6,000+ emails processed through the ingestion pipeline
- 26-file AI recall package with version lineage through `v10.4`

## What Makes Stonewall Different

### 1. Flat-file searchable database
`catalog/manifest.md` functions as a real operating database in Markdown. Every artifact receives a durable ID, date, type, case link, entity references, pattern references, and summary text, with derivative indexes for date, case, character, pattern, and email searches.

### 2. CLI intelligence layer
The public CLI demonstrates how a litigation corpus can be queried without a database server:

```bash
$ python scripts/stonewall.py stats
total rows      : 1206
active          : 1122
analyzed        : 731 (65.2%)
patterns        : 197
characters      : 173
cases           : 64
```

```bash
$ python scripts/stonewall.py find "deposition"
A0198  Public Deposition Transcript      2025-02-28  deposition
A0441  Expert Deposition Outline         2025-07-16  deposition
A0917  Corporate Representative Prep     2026-01-11  deposition
```

```bash
$ python scripts/stonewall.py validate --strict
0 error(s), 153 warning(s) across 1206 rows
```

### 3. AI skill architecture
Stonewall’s “brain” is not a vector database or a hidden memory layer. It is a versioned recall architecture composed of codex files that point the agent to primary sources, then instruct it to read before asserting facts. The public showcase includes the current version lineage through `v10.4` and highlights the separation between recall, validation, and source reading.

### 4. Automated ingestion pipeline
The platform ingests documents from OneDrive and related litigation reservoirs, converts PDFs and DOCX files into Markdown sidecars, normalizes email exports, and prepares sanitized derivatives for downstream indexing and synchronization.

### 5. Multi-platform sync
Stonewall coordinates across GitHub, Notion, and OneDrive:

- GitHub stores the corpus, scripts, QC gates, and deployable static surfaces
- Notion holds case-management views and operational registries
- OneDrive acts as the upstream document reservoir

### 6. Verification and QC automation
Public quality gates mirror production discipline. Repository consistency checks, manifest validation, ontology enforcement, and deploy-time sanitization guards make sure the published artifact is both structurally sound and safe to expose.

### 7. Phenomenology registry
Stonewall maintains a 197-pattern behavioral taxonomy that can be instantiated across artifacts and tracked longitudinally. The public showcase preserves the taxonomy while removing identifying matter context.

### 8. Static portal
The included portal demonstrates how a multi-page operational dashboard can run as a fully static site from JSON snapshots alone. Dashboard, cases, deadlines, artifacts, patterns, characters, and billing-style workflows all render without a backend dependency in the public build.

## Operator Value

- **Daily dossier**: a working lawyer can open the system and immediately see what changed, what is urgent, and what deserves attention today
- **Deadline intelligence**: the platform converts scattered source records into a usable runway for upcoming work, not just a passive calendar
- **Workflow readiness**: the same corpus supports deposition prep, mediation prep, intake triage, search under time pressure, and billing reconstruction
- **Notion as command surface**: the repo remains the durable corpus while Notion becomes the live operations layer for matter posture, archive links, task runway, and daily control
- **DataGavel workflow readiness**: chronology, records, and damages notes can be staged into a report-ready packet instead of rebuilt from scratch every time a valuation workflow begins
- **Live deposition tailoring**: the same indexed corpus can tighten outlines in real time by surfacing prior statements, chronology gaps, and issue clusters while the witness is still in the room
- **Production guarantees**: validation gates, repo consistency checks, and sanitization guards make the public artifact trustworthy by design

## Tactical Workflow Layer

### Notion as the operator layer

Stonewall is strongest when the repo and Notion do different jobs well. The repo keeps the durable evidence trail and searchable archive; Notion turns that into a live command surface for deadlines, matter posture, archive relations, and daily workflow control.

```bash
python scripts/notion_wire_cases.py
python scripts/notion_case_dates.py
node scripts/repo_data_push.mjs
```

### DataGavel workflow readiness

The platform is designed to make structured report workflows easier to feed. Records can be pulled into a clean chronology, treatment trails can be checked, and damages notes can be staged into a packet that is ready for a specialized report workflow rather than requiring another scavenger hunt.

```text
records pulled
→ chronology checked
→ treatment ledger aligned
→ damages notes staged
→ report packet ready
```

### Live deposition outline tailoring

Because transcripts, filings, emails, and reference notes all live in the same indexed corpus, the operator can tighten the next section of a deposition outline while testimony is still unfolding. That is a materially different product story from simple archival storage.

```bash
python scripts/stonewall.py find "corporate representative"
python scripts/stonewall.py timeline --start 2025-02-01 --end 2025-02-28
python scripts/stonewall.py show A1104
```

## Architecture

```text
OneDrive / Source Reservoir
            |
            v
      Ingestion Layer
  ingest_onedrive.py
  transcribe_repo_pdfs.py
  docx_to_verbatim_md.py
            |
            v
      Processing Layer
  sidecars / normalization / tagging
            |
            v
        Notion Sync
  notion_wire_cases.py
  notion_wire_batch.py
  notion_case_dates.py
            |
            v
         Catalog Layer
  manifest.md + derivative indexes
            |
            v
          CLI Query
  stats / find / case / pattern / timeline
            |
            v
        Static Portal
  site-data.json + docs/portal/data/*.json
```

## Repository Surfaces

```text
docs/
  showcase.html        public landing page
  index.html           command dashboard shell
  site-data.json       aggregate showcase metrics
  portal/
    index.html         static SPA entrypoint
    data/*.json        sanitized public demo data

catalog/
  manifest.md          flat-file database
  index_by_*.md        derivative indexes

scripts/
  stonewall.py         stdlib-only CLI interface
  verify_repo_consistency.py
  pre_pr_check.py
  repo_sweep.py
```

## Public Safety Model

This showcase is designed to demonstrate system architecture, not reveal case content.

- Real client names are removed
- Case captions are replaced by generic matter names
- Character identities are converted to role-based labels
- Email addresses, phone numbers, and internal IDs are omitted
- Artifact dates, types, counts, and structural relationships are preserved where safe

The GitHub Pages deploy workflow includes additional guards to block known internal terms from appearing in the public `docs/portal/data/` bundle.

## Static Deployment

The public site is built directly from the repository’s `docs/` directory through GitHub Pages. No frontend build step is required.

- `docs/showcase.html` is the public landing page
- `docs/index.html` is the dashboard shell
- `docs/portal/` hosts the static SPA demo
- `.github/workflows/static.yml` deploys the sanitized bundle on push to `main`
- `README.md` carries the long-form public narrative that can be mirrored into a showcase repo or GitBook-style documentation surface

## Why This Matters

Stonewall is a proof point that a litigation team does not need a heavyweight proprietary platform to build durable document intelligence. With disciplined catalogs, strong ingestion, explicit validation, and a static deployment model, a solo builder can produce a system that is searchable, inspectable, versioned, and operationally useful at real scale.
