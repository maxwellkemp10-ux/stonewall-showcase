#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

require_cmd() {
  local cmd="$1"
  local install_hint="$2"
  if ! command -v "${cmd}" >/dev/null 2>&1; then
    echo "[ERROR] Missing required command: ${cmd}" >&2
    echo "[HINT] ${install_hint}" >&2
    exit 1
  fi
}

ensure_python_package() {
  local import_name="$1"
  local package_name="$2"
  if ! python3 -c "import ${import_name}" >/dev/null 2>&1; then
    echo "[INFO] Installing missing Python package: ${package_name}"
    python3 -m pip install --user "${package_name}"
  else
    echo "[OK] Python package available: ${package_name}"
  fi
}

ensure_uv_cli() {
  if command -v uv >/dev/null 2>&1; then
    echo "[OK] uv available on PATH"
    return
  fi

  if [[ -x "${HOME}/.local/bin/uv" ]]; then
    echo "[OK] uv installed at ${HOME}/.local/bin/uv"
    return
  fi

  echo "[INFO] Installing missing CLI: uv"
  python3 -m pip install --user uv
}

echo "[INFO] Bootstrapping Stonewall developer environment"
echo "[INFO] Repo root: ${REPO_ROOT}"

require_cmd python3 "Install Python 3.12+ and re-run this script."
require_cmd node "Install Node.js 22+ and re-run this script."

echo "[INFO] Runtime versions"
python3 --version
node --version

ensure_uv_cli
ensure_python_package docx python-docx

echo "[INFO] Validating uv execution path"
if command -v uv >/dev/null 2>&1; then
  uv --version
else
  "${HOME}/.local/bin/uv" --version
  echo "[WARN] uv is not on PATH. Add this for convenience:"
  echo "       export PATH=\"${HOME}/.local/bin:\$PATH\""
fi

echo "[DONE] Environment bootstrap complete"
