---
description: Live surface map, sync rules, and control-plane workflow.
---

# 🔀 Notion Sync Protocol — v8.8 — Updated 2026-04-08

{% include ".gitbook/includes/global-control-deck.md" %}

{% include ".gitbook/includes/audit-source-protocol.md" %}

<a href="references/execution-and-systems/tactical-prompts/" class="button secondary" data-icon="bolt">Tactical prompts</a>

Use this reference when the user asks to sync Stonewall or legal-matter information into Notion.

## 2026-04-08 Surface Note

The `corpus-hardening` merge changed repo-side corpus quality and routing, but it did **not** change the live Notion IDs below. Treat the surfaces in this file as still-live; the update here is simply to record that the repo memory and retrieval layers were refreshed while the Notion surface map remained stable.

## Current Live Database Surfaces (verified 2026-03-31)

| Surface           | Page ID                                | Data Source                                         |
| ----------------- | -------------------------------------- | --------------------------------------------------- |
| Legal Matters     | `d96a8582-ddba-42a8-a396-b595bc9b5034` | `collection://66396fb5-82db-40a7-ab24-2e3a225a6d3c` |
| All Email v2      | `450d0313-15c4-4459-afca-a5c0b7b952d2` | `collection://8cdb2f05-752d-4911-8405-d374685cf37b` |
| Stonewall Archive | `37bb53a0-cfad-476d-b715-4bca6b310660` | `collection://28206687-1565-4ca1-85ad-510964e3250d` |
| Stonewall Tasks   | `0ecc4db1-c622-49a9-9365-0d1f458e5b5a` | `collection://551a80f5-d9c3-45fb-9b7c-ca32491a52c5` |
| My Tasks          | `43b0d5e0-c2fe-4c8a-a43a-f3bd796693ae` | —                                                   |

## Current Live Page Surfaces

| Surface                | Page ID                                |
| ---------------------- | -------------------------------------- |
| QB1 Command Center     | `2dec0fdb-2529-8133-a01b-ea072887809b` |
| Implementation Surface | `32ac0fdb-2529-815c-b784-e6c628002bb2` |

## Legal Matters View Architecture (rebuilt 2026-03-31)

### Primary Working Set (17 views)

1. Command Deck — primary operational view, deadline + description + all key fields
2. All Cases — unfiltered, sorted by Phase
3. Upcoming Deadlines — calendar by Next Deadline
4. 🔥 Next 30 Days — date-bounded runway: `Next Deadline IS NOT EMPTY`, `>= window start`, `<= window end`, `Status != Closed`, `Phase != Settled`. **Note:** date range is hardcoded (currently 3/31-4/30/26); update monthly via `notion-update-view` DSL.
5. Trial Runway — Trial Prep / Trial phase, shows Next Deadline Item
6. Settlement Tracker — Settlement / Closed / Settled / Mediation phase
7. DataGavel Queue — DG work queue (Not Started / Pending / In Progress / In Prep / empty)
8. Task Radar — cases WITH Stonewall Tasks relations
9. Legal Hold Tracker — Active Hold / Release Pending / Active
10. Pre-Suit Intake — New Intake / Pre-Suit
11. Backfill Queue — cases missing key identity fields (Plaintiff, Adjuster, OC, Driver, Claim#, Case#)
12. Mediation Pipeline — Mediation status or Mediation/Settlement phase, shows Next Deadline Item
13. Mediation Calendar — calendar by Mediation Date
14. 📅 Trial Calendar — calendar by Trial Date
15. 📋 Depo Tracker — Plaintiff Depo checked, sorted by Depo Date
16. 🏷️ Claim Number Index — sorted by Claim Number for quick lookups
17. 📄 Partner Export — unfiltered flat table, sorted by Next Deadline, all key fields

### QA Canary Layer

| View                 | Database          | Purpose                                                     |
| -------------------- | ----------------- | ----------------------------------------------------------- |
| Deadline Blind Spots | Legal Matters     | Active matters with no `Next Deadline`                      |
| Task Link Gaps       | Legal Matters     | Active matters with no `Stonewall Tasks` tether             |
| Archive Link Gaps    | Legal Matters     | Active matters with no `📎 Archive Docs` relations          |
| Artifact Link Gaps   | Stonewall Archive | Archive records with `Cases` text but no `⚖️ Case` relation |

### Cross-Database Relation

* Stonewall Archive `⚖️ Case` → Legal Matters (two-way relation, enabled 3/31/26)
* Legal Matters `📎 Archive Docs` → Stonewall Archive (reciprocal property)

### Relegated Views (not hard-deleted — connector lacks view deletion)

Archive — Empty Dashboard, Archive — Legacy All Cases, Archive — Phase Board, Archive — Status Board, Archive — Adjuster Board, Archive — Trial Timeline, Archive — Active Caseload (relegated 3/31/26 — redundant with Command Deck), Analytics — Status Breakdown, Analytics — Phase Pipeline, Analytics — OC Firm Map, Analytics — Adjuster Split, Analytics — Reserve Distribution, Analytics — Incurred by Phase.

## Retired Targets (DO NOT USE)

* ~~`667f9a80`~~ (old Corpus Compendium DB)
* ~~`329d8306`~~ (old Command Center page)
* ~~`collection://cb6644e3-...`~~ (old corpus data source)
* ~~`collection://7061697b-...`~~ (old Legal Matters collection)

## Operating Rules

* Update both properties and content when syncing.
* Preserve canon: names, chronology, and attribution must match the Stonewall references.
* When a task affects a Legal Matters database entry and the Command Center page, keep both in sync.
* Prefer exact page or property edits over vague summaries.
* Use collection:// URIs for database queries; use page IDs for Notion MCP plugin page operations.
* Use the QA canary views to detect operational drift before it compounds.

## Practical Workflow

1. Use the live workspace surfaces first for corpus search, filename retrieval, and cluster discovery.
2. Fetch the target database, data source, or page before editing when the schema or current content matters.
3. Confirm the exact property names from the fetched schema before updating database records.
4. Update page content as well as structured properties when the user asks to sync.
5. Use Stonewall references to avoid identity drift or chronology mistakes.
6. After sync operations, spot-check QA canary views to confirm no new gaps were introduced.
