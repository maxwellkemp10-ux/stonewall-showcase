# Stonewall — Legal Document Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Notion API](https://img.shields.io/badge/Notion-API-000000?logo=notion&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-AI%20Skills-D97757)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)

Stonewall is a legal document intelligence platform built as a litigation control plane. It turns a large working corpus into something a lawyer can search, validate, synchronize, and operate against in real time, using flat files, disciplined indexing, AI recall architecture, and static deployment surfaces.

The result is a system that feels less like a document dump and more like an operating environment: one place to understand portfolio scale, workflow readiness, deadline posture, report-packet preparation, and witness-prep leverage.

## Live Surfaces

- Showcase: https://maxwellkemp10-ux.github.io/stonewall-showcase/
- Official brief: https://maxwellkemp10-ux.github.io/stonewall-showcase/official-brief.html
- Portal demo: https://maxwellkemp10-ux.github.io/stonewall-showcase/portal/
- GitBook edition: https://maxwell-kemp.gitbook.io/stonewall-qb3/stonewall-showcase/quarterback/

## Snapshot

- 1,200+ artifacts cataloged in a flat-file manifest
- 60+ active matters represented in the showcase model
- 197 behavioral patterns indexed and cross-referenced
- 170+ character profiles represented through role-based abstractions
- 6,000+ emails processed through the ingestion pipeline
- 26-file AI recall package with version lineage through `v10.4`

## Product Thesis

Stonewall starts from a simple proposition: legal operations do not need to begin with a heavyweight proprietary platform. They can begin with a rigorously structured corpus.

Once every artifact is cataloged with durable IDs, dates, types, matter links, entity references, pattern references, and summary metadata, the same archive can serve multiple jobs at once:

- search layer
- validation layer
- operator layer
- publishing layer
- AI retrieval layer

That is why the platform feels coherent. The same source of truth drives the CLI, the portal, the official brief, the GitBook narrative, and the AI recall system.

## Innovation Stack

### 1. Flat-file searchable database

`catalog/manifest.md` functions as a real operating database in Markdown. It remains human-readable, Git-trackable, grep-queryable, and structurally inspectable while still carrying durable IDs, dates, types, matter links, entity links, pattern links, and summary text.

### 2. CLI intelligence layer

The stdlib-only CLI exposes stats, search, case, timeline, pattern, validation, and doctor workflows directly from the corpus.

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

### 3. AI recall architecture

Stonewall’s brain is a versioned recall system composed of codex files that route the model to the right source surface before it speaks with confidence. It is explicit, inspectable, and portable.

### 4. Automated ingestion pipeline

PDFs, DOCX files, screenshots, and email exports are converted into searchable derivatives and normalized metadata. The archive stays alive after ingestion instead of becoming a dead reservoir of attachments.

### 5. Multi-platform sync

GitHub stores the durable corpus, Notion acts as the operator layer, and the source reservoir feeds the ingestion loop. Cross-reference manifests and sync scripts keep the system aligned across surfaces.

### 6. Verification and QC automation

Repo consistency checks, ontology enforcement, sidecar audits, and deployment guards make the output trustworthy by design.

### 7. Phenomenology registry

Stonewall maintains a 197-pattern behavioral taxonomy that can be instantiated across artifacts and traced longitudinally across the corpus.

### 8. Static portal

The portal demonstrates how a multi-page operational dashboard can run as a fully static site from JSON snapshots alone, without losing the feeling of a serious application.

## Workflow Leverage

The strongest product story is operational, not archival.

- Daily dossier: one surface for what changed, what matters, and what deserves attention today
- Deadline intelligence: runway instead of a passive list of dates
- Notion operator layer: a live matter-control surface for posture, archive links, and task flow
- DataGavel workflow readiness: chronology, treatment trail, and damages notes staged into a coherent packet
- Live deposition tailoring: outlines tightened in real time from indexed statements, chronology gaps, and issue clusters
- Durable institutional memory: search and structure that compound over time rather than reset with every new matter

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

## Publication Stack

Stonewall publishes through three coordinated surfaces:

- GitHub Pages for immediate visual clarity and shareability
- `official-brief.html` for the printable and boardroom-safe edition of the thesis
- GitBook for the durable long-form narrative edition of the same product logic

These surfaces should feel like one argument told in three tempos: immediate, formal, and durable.

## Why It Matters

Stonewall shows that a small team or even a single disciplined operator can build serious legal document intelligence without waiting for institutional permission, heavyweight software budgets, or opaque platform abstractions. The archive is the product substrate. The control plane emerges from the archive. Everything else is presentation.
