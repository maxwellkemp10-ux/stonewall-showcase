# Stonewall CLI

> Purpose-built command-line interface for corpus diagnostics, full-text search, and operational health checks.

## Overview

The Stonewall CLI (`stonewall.py`) is the primary operator interface for interacting with the document corpus from the command line. It provides fast, scriptable access to corpus statistics, artifact search, case lookups, manifest validation, and health diagnostics — all without requiring a browser or external API calls.

The CLI is designed to be used both interactively during daily operations and programmatically within CI/CD pipelines as part of the pre-merge verification gate.

---

## Commands

### `stats` — Corpus Statistics

Returns a summary of the indexed corpus, including total artifact count, format breakdowns, active vs. archived counts, and coverage metrics.

```bash
python scripts/stonewall.py stats
```

**Example output:**
```
Corpus Summary
──────────────
Total artifacts:    1,106 active (1,190 manifest rows)
Formats:            PDF: 612 | DOCX: 287 | XLSX: 94 | Other: 113
Coverage:           96% analyzed
Last updated:       2026-04-08
```

---

### `search` — Full-Text Search

Searches across all indexed artifacts by keyword or phrase. Supports result limiting and JSON output for pipeline integration.

```bash
# Basic search
python scripts/stonewall.py search "keyword"

# Limit results
python scripts/stonewall.py search "keyword" --limit 10

# JSON output for scripting
python scripts/stonewall.py search "keyword" --json
```

**Example output:**
```
3 results for "keyword"
──────────────────────
1. sources/documents/report-2026-03-15.md  (line 42)
   ...the keyword appears in the context of quarterly review...

2. sources/correspondence/memo-2026-02-20.md  (line 7)
   ...referencing the keyword in connection with compliance...

3. sources/analysis/summary-2026-01-10.md  (line 128)
   ...keyword usage tracked across the reporting period...
```

---

### `case` — Case Lookups

Queries matter-specific data by keyword. Returns matching case references, associated artifacts, and current status metadata.

```bash
python scripts/stonewall.py case "smith"
```

---

### `validate` — Manifest Validation

Verifies manifest integrity by checking that every manifest entry corresponds to an existing file, that all files in tracked directories appear in the manifest, and that no duplicates or naming violations exist.

```bash
python scripts/stonewall.py validate
```

**Example output:**
```
Manifest Validation
───────────────────
Manifest rows:      1,190
Active entries:     1,106
Missing files:      0
Orphaned files:     0
Duplicates:         0
Status:             ✅ PASS
```

---

### `health` — Health Diagnostics

Runs a comprehensive system health check covering corpus integrity, index freshness, gap analysis, and configuration validation.

```bash
python scripts/stonewall.py health
```

**Example output:**
```
Health Check
────────────
Corpus integrity:   ✅ PASS
Manifest sync:      ✅ PASS
Index freshness:    ✅ Updated within 24h
Coverage gaps:      2 items pending analysis
Config validation:  ✅ All required env vars set
Overall:            ✅ HEALTHY
```

---

## Output Formats

| Flag | Description |
|------|-------------|
| `--json` | Returns structured JSON output suitable for scripting and pipeline consumption |
| `--limit N` | Limits search results to the top N matches |

---

## CI/CD Integration

The Stonewall CLI is invoked as part of the pre-PR verification gate (`verify_all.py`). Before any pull request is merged, the following checks run automatically:

1. `stonewall.py validate` — ensures manifest integrity
2. `stonewall.py health` — confirms system health
3. Full test suite execution
4. Repo consistency verification

This ensures that no merge introduces manifest drift, orphaned files, or corpus integrity violations.

---

## Design Principles

* **No external API calls required** — operates entirely on the local corpus and manifest
* **Scriptable** — JSON output and exit codes support automation
* **Fast** — designed for sub-second responses on corpora up to 2,000+ artifacts
* **Safe** — read-only operations; the CLI never modifies corpus data
