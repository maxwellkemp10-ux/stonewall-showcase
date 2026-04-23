# Development Environment & Innovation Surface Workflow

This repository is optimized for script-first development across Python and Node surfaces.

## 1) Bootstrap once per machine

Run:

- `make bootstrap`

What it does:

- Verifies required runtimes are installed (`python3`, `node`)
- Installs missing `uv` CLI (user-local) when needed
- Installs missing `python-docx` (required by `scripts/docx_to_md.py`)
- Prints versions and readiness status

## 2) Run innovation surface smoke checks

Run:

- `make smoke`

What it validates:

- Node test surfaces
- Python test surfaces
- Repo consistency and sweep surfaces
- Ingestion report surface (`ingest_onedrive.py report`)
- Tactical brief rendering surface (with isolated synthetic inputs)
- DOCX conversion surface
- Email consolidator CLI surface (in isolated temp tree)

The smoke script is designed to avoid mutating tracked repository state.

## 3) Fast command surface map

- `make test-node` — Node tests for helper/consolidator logic
- `make test-python` — Python tests for ingestion/brief/consistency
- `make verify` — repository consistency report
- `make repo-sweep` — repository sweep report
- `make ingest-help` — ingestion CLI command map
- `make brief-help` — tactical brief CLI command map

## 4) Recommended workflow for new integrations

1. `make bootstrap`
2. Implement changes for one surface at a time (`scripts/*` + `tests/*`)
3. Run targeted checks (`make test-node` or `make test-python`)
4. Run full integration confidence check: `make smoke`
5. Commit once smoke passes

## 5) Optional PATH convenience

If `uv` is installed at `~/.local/bin/uv` and not found on PATH, add:

- `export PATH="$HOME/.local/bin:$PATH"`
