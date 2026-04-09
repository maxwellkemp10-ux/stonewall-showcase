# 🧩 Stonewall Ontology v1.0

> The control plane needs a contract. This is it.

This document freezes the Stonewall entity model: the seven logical types the corpus is built from, the relations between them, and the invariants that any future ingest, validator, or Notion sync must honor. The machine-readable form lives at `references/schemas/stonewall_ontology_v1.json`. This prose companion explains the rules in the voice of the domo.

**Version:** 1.0.0 **Frozen:** 2026-04-05 **Authority:** This schema governs the manifest, the index files, the `stonewall` CLI, and all future Notion payloads. The codices still win on identity, chronology, and naming — this schema describes _shape_, not truth.

***

## Why we freeze the ontology

We are past the sketch phase. The repo has 1,190 manifest rows, 1,106 active rows, 197 live patterns, 11 crown matters, and a validated control plane with zero strict errors. Drift is the enemy now — a stray type value, a renamed case, a character alias that slips past the cast codex, and the graph quietly rots. A versioned schema turns the control plane into something you can test against.

The rule: **every artifact that enters the manifest, every row shipped to Notion, and every brief the CLI composes must validate against v1.**

***

## The seven entities

### 1. Artifact

The atomic unit. One row in `catalog/manifest.md` is one artifact.

**Required fields:** `id`, `type`, `summary`, `analyzed`.

**Identifier rule:** `^A[0-9]{3,4}$`, sequential. Tombstoned IDs (e.g., A029, A087) are retained, never reissued. Gaps are sacred.

**Type vocabulary:** see the `ArtifactType` enum in the JSON schema. Compound forms like `transcript/call` or `screenshot/iMessage` are permitted for now but discouraged — they should be promoted to first-class types once they stabilize, or collapsed into a subtype field in a future version.

**Sidecar convention:** `.pdf.md` and `.docx.md` markdown companions inherit their parent's A-ID. They do not get their own rows.

### 2. Case

A matter. Crown, secondary, resolved, reference, or multi.

Canonical names live in `case_codex.md`. The manifest's `Case` column is a free-text field today but will be validated against the case codex's known labels in v1.1. `Multi-Case` and the em-dash sentinel are reserved values.

### 3. Person (Character)

A named actor in the corpus. Canonical names come from `cast_codex.md`.

**Identity locks are schema-level.** Kerry Coles is MALE. Nicole is not a Satan. Mr. Bone is not Mr. Bill. Dan Bubley is a hockey coach, not a litigation character. Karen Lee is QB1's mother. These aren't suggestions — they are validator failures. The `identityLocks` field on Person exists to let the validator check that no manifest row misattributes a locked identity.

### 4. Pattern

A phenomenology entry. 197 total, organized in eleven bands:

| Band              | Range   |
| ----------------- | ------- |
| Core              | 1–97    |
| Championship      | 98–120  |
| Cross-Artifact    | 121–126 |
| Formation         | 127–130 |
| Post-Blitzkrieg   | 131–141 |
| Corpus Compendium | 142–152 |
| Stomping the Yard | 153–172 |
| Ostrich           | 173–176 |
| CME / Expert      | 177–178 |
| Approval Theater  | 179–184 |
| Chapter XIII-XIV  | 185–197 |

Patterns in the manifest are comma-separated numbers. The validator checks that every cited number exists in `phenomenology_registry.md`.

### 5. Event

A dated moment with a chronology lock. The Manifesto (5:29 PM, 2026-01-09) always precedes Die Glocke (6:21 PM, same day). Snappening 1 precedes Snappening 2. UPS meeting rescheduled FROM 3/19 TO 3/24, never reversed.

Events are artifacts whose `type = "event"`. The `chronologyLock` field records the constraint; the validator refuses to let two events violate a stated lock.

### 6. Relation

An edge in the corpus graph. The manifest encodes relations implicitly:

| Manifest column | Predicate                     |
| --------------- | ----------------------------- |
| Characters      | `features_character`          |
| Patterns        | `instantiates_pattern`        |
| Case            | `belongs_to_case`             |
| (Summary)       | `documents_event` (heuristic) |

Two file-level predicates live outside the manifest:

* `sidecar_of` — `.pdf.md` → parent `.pdf`
* `supersedes` / `derives_from` — version chains across codex snapshots

### 7. Run

An audit record. Every CLI invocation that mutates state (ingest, sync, validate with `--fix`) writes one `Run` record. This is the append-only event log that makes ingest and sync replayable. v1.0 defines the shape; the persistence layer lands in v1.1.

***

## Invariants

The validator enforces these. Violations are fail-closed.

1. **ID uniqueness.** Every non-tombstoned row has a unique `A\d{3,4}` ID.
2. **Type in vocabulary.** Every `type` value appears in the enum.
3. **Date shape.** Dates are ISO `YYYY-MM-DD` (preferred), `YYYY-MM` for month-granularity rollups like monthly email archives, or the em-dash sentinel. Legacy `M/D/YY` values are auto-normalized at load time.
4. **Analyzed flag.** `yes` or `no`, nothing else.
5. **File exists (when claimed).** If the `file` field names a repo path, the file must exist or be explicitly tombstoned.
6. **Pattern numbers resolve.** Every cited pattern number maps to an entry in `phenomenology_registry.md`.
7. **Chronology locks hold.** Manifesto < Die Glocke. Snappening 1 < Snappening 2. UPS 3/19 → 3/24 (never reversed).
8. **Identity locks hold.** No row contradicts a declared identity lock.

***

## Versioning

* **Patch (1.0.x):** clarifications, doc fixes, new enum values for types that were already observed in the manifest.
* **Minor (1.x.0):** new optional fields, new predicates, new entity subtypes, strengthened validation.
* **Major (x.0.0):** removed fields, renamed entities, relaxed invariants.

Each bump writes a migration note in this file and a dated entry in `references/SKILLS_VERSION_CONTROL_MANIFEST.md`.

***

## Relationship to existing codices

This ontology does not replace the codices — it formalizes the _contract_ they already imply.

| Codex                         | Ontological role                    |
| ----------------------------- | ----------------------------------- |
| `cast_codex.md`               | Person canon + identity locks       |
| `case_codex.md`               | Case canon + tier assignment        |
| `phenomenology_registry.md`   | Pattern canon + band assignment     |
| `artifact_codex.md`           | Event chronology + chronology locks |
| `deposition_codex.md`         | Event subtype: depositions          |
| `tactical_legal_standards.md` | Output shape, not entity shape      |

The codices win on truth. This schema wins on shape. When they disagree, update the codex first, then bump the schema to match.

***

## Consumers (v1.0)

* `scripts/stonewall_cli/` — the `stonewall` CLI's validator and graph.
* `scripts/verify_repo_consistency.py` — already enforces file/manifest parity; will add ontology validation in the next pass.
* Future Notion sync — payload builders validate against v1 before POST.
