#!/usr/bin/env python3
"""Lightweight CI guardrails for syntax + deployment/env contract checks."""

from __future__ import annotations

import json
import py_compile
import subprocess
import sys
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_ENV_KEYS = {
    "NOTION_TOKEN",
    "NOTION_LEGAL_MATTERS_DB",
    "NOTION_ALL_EMAIL_DB",
    "NOTION_ARCHIVE_DB",
    "ONEDRIVE_PERSONAL_ROOT",
    "ONEDRIVE_FIRM_ROOT",
    "TELEGRAM_BOT_TOKEN",
}


def read_env_example_keys(path: Path) -> set[str]:
    keys: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :]
        if "=" not in line:
            continue
        key = line.split("=", 1)[0].strip()
        if key:
            keys.add(key)
    return keys


def assert_env_contract() -> None:
    env_example = REPO_ROOT / ".env.example"
    if not env_example.exists():
        raise SystemExit("[FAIL] Missing required file: .env.example")
    keys = read_env_example_keys(env_example)
    missing = sorted(REQUIRED_ENV_KEYS - keys)
    if missing:
        raise SystemExit(
            "[FAIL] .env.example missing required keys: " + ", ".join(missing)
        )
    print("[OK] .env.example contract includes required keys")


def assert_json_file(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"[FAIL] Missing required config: {path.relative_to(REPO_ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def assert_toml_file(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"[FAIL] Missing required config: {path.relative_to(REPO_ROOT)}")
    with path.open("rb") as handle:
        return tomllib.load(handle)


def assert_deploy_configs() -> None:
    if (REPO_ROOT / "railway.json").exists():
        raise SystemExit(
            "[FAIL] railway.json must not exist; Railway bot start command is managed in Railway service settings."
        )

    vercel = assert_json_file(REPO_ROOT / "vercel.json")
    rewrites = vercel.get("rewrites", [])
    root_rewrite = any(
        item.get("source") == "/" and item.get("destination") == "/docs/index.html"
        for item in rewrites
        if isinstance(item, dict)
    )
    portal_rewrite = any(
        item.get("source") == "/portal" and item.get("destination") == "/docs/portal/index.html"
        for item in rewrites
        if isinstance(item, dict)
    )
    if not root_rewrite or not portal_rewrite:
        raise SystemExit("[FAIL] vercel.json is missing required root/portal rewrites")

    wrangler = assert_toml_file(REPO_ROOT / "wrangler.toml")
    if wrangler.get("main") != "_worker.js":
        raise SystemExit("[FAIL] wrangler.toml main must be _worker.js")
    assets = wrangler.get("assets", {})
    if assets.get("directory") != "./docs" or assets.get("binding") != "ASSETS":
        raise SystemExit("[FAIL] wrangler.toml assets must target ./docs with ASSETS binding")

    worker_path = REPO_ROOT / "_worker.js"
    if not worker_path.exists():
        raise SystemExit("[FAIL] Missing Cloudflare worker file: _worker.js")
    worker_source = worker_path.read_text(encoding="utf-8")
    if "env.ASSETS.fetch" not in worker_source:
        raise SystemExit("[FAIL] _worker.js must fetch static assets via env.ASSETS.fetch")

    replit = REPO_ROOT / ".replit"
    if not replit.exists():
        raise SystemExit("[FAIL] Missing Replit config: .replit")
    replit_text = replit.read_text(encoding="utf-8")
    if "scripts/serve_static.py" not in replit_text:
        raise SystemExit("[FAIL] .replit must run scripts/serve_static.py")

    replit_nix = REPO_ROOT / "replit.nix"
    if not replit_nix.exists():
        raise SystemExit("[FAIL] Missing Replit nix config: replit.nix")

    print("[OK] Deployment configs validated (Vercel/Cloudflare/Replit + Railway guard)")


def iter_python_files() -> list[Path]:
    return sorted(
        path
        for root in (REPO_ROOT / "scripts", REPO_ROOT / "tests")
        for path in root.rglob("*.py")
        if path.is_file()
    )


def iter_node_files() -> list[Path]:
    node_files: list[Path] = sorted(
        path
        for root in (REPO_ROOT / "scripts", REPO_ROOT / "tests")
        for path in root.rglob("*.mjs")
        if path.is_file()
    )
    worker = REPO_ROOT / "_worker.js"
    if worker.exists():
        node_files.append(worker)
    return node_files


def assert_python_syntax() -> None:
    for path in iter_python_files():
        py_compile.compile(str(path), doraise=True)
    print("[OK] Python syntax check passed")


def assert_node_syntax() -> None:
    node_bin = "node"
    for path in iter_node_files():
        cmd = [node_bin, "--check", str(path)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            sys.stderr.write(proc.stderr or proc.stdout)
            raise SystemExit(
                f"[FAIL] Node syntax check failed: {path.relative_to(REPO_ROOT)}"
            )
    print("[OK] Node syntax check passed")


def main() -> int:
    assert_env_contract()
    assert_deploy_configs()
    assert_python_syntax()
    assert_node_syntax()
    print("[DONE] CI guardrails passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
