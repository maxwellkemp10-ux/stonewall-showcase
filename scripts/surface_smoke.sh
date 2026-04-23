#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

UV_BIN=""
if command -v uv >/dev/null 2>&1; then
  UV_BIN="$(command -v uv)"
elif [[ -x "${HOME}/.local/bin/uv" ]]; then
  UV_BIN="${HOME}/.local/bin/uv"
fi

TMP_DIR="$(mktemp -d)"
EMAIL_TMP_DIR="$(mktemp -d)"
EMAIL_SCRIPT_ROOT="${EMAIL_TMP_DIR}/smoke-root"

cleanup() {
  rm -rf "${TMP_DIR}" "${EMAIL_TMP_DIR}"
}
trap cleanup EXIT

echo "[INFO] Running Stonewall surface smoke checks"
echo "[INFO] Repository: ${REPO_ROOT}"

echo "[STEP] Node unit surfaces"
(
  cd "${REPO_ROOT}"
  node --test tests/qb1_tracker_helpers.test.mjs tests/email_consolidator.test.mjs
)

echo "[STEP] Python unit surfaces"
(
  cd "${REPO_ROOT}"
  python3 -m unittest \
    tests.test_ingest_onedrive \
    tests.test_verify_repo_consistency \
    tests.test_tactical_brief \
    tests.test_legal_matters_offline_backfill
)

echo "[STEP] Repo consistency/reporting surfaces"
(
  cd "${REPO_ROOT}"
  python3 scripts/verify_repo_consistency.py --output "${TMP_DIR}/repo_consistency_report.json"
  python3 scripts/repo_sweep.py --output "${TMP_DIR}/repo_sweep_report.json"
)

echo "[STEP] Intake report surface"
(
  cd "${REPO_ROOT}"
  if [[ -n "${UV_BIN}" ]]; then
    "${UV_BIN}" run python scripts/ingest_onedrive.py report --output "${TMP_DIR}/onedrive_status_report.md"
  else
    python3 scripts/ingest_onedrive.py report --output "${TMP_DIR}/onedrive_status_report.md"
  fi
)

echo "[STEP] Tactical brief rendering surface"
python3 -c "from pathlib import Path; d=Path('${TMP_DIR}'); (d/'manifest.md').write_text('', encoding='utf-8'); (d/'case_dates.json').write_text('[]', encoding='utf-8'); (d/'case_index.md').write_text('', encoding='utf-8')"
(
  cd "${REPO_ROOT}"
  python3 scripts/tactical_brief.py today \
    --manifest "${TMP_DIR}/manifest.md" \
    --case-dates "${TMP_DIR}/case_dates.json" \
    --case-md "${TMP_DIR}/case_index.md" \
    --report "${TMP_DIR}/repo_consistency_report.json"
)

echo "[STEP] DOCX conversion surface"
python3 -c "from docx import Document; d=Document(); d.add_paragraph('Stonewall smoke test'); d.save('${TMP_DIR}/sample.docx')"
(
  cd "${REPO_ROOT}"
  python3 scripts/docx_to_md.py "${TMP_DIR}/sample.docx"
)

echo "[STEP] Email consolidator CLI surface (isolated temp tree)"
mkdir -p "${EMAIL_SCRIPT_ROOT}/scripts" "${EMAIL_SCRIPT_ROOT}/sources/emails"
cp "${REPO_ROOT}/scripts/email_consolidator.mjs" "${EMAIL_SCRIPT_ROOT}/scripts/email_consolidator.mjs"
printf 'From,To,Subject,Date,Body\n"alice@example.com","bob@example.com","Test Subject","4/1/2026 9:00 AM","Sent: Tuesday, April 1, 2026 9:00 AM"\n' > "${EMAIL_SCRIPT_ROOT}/sources/emails/Inbox 4.01.26.csv"
node "${EMAIL_SCRIPT_ROOT}/scripts/email_consolidator.mjs" --json >/dev/null

echo "[DONE] Surface smoke checks passed"
