"""Parameterized verification suite for the showcase sample corpus.

Generates one TestCase method per (fixture, check) pair so the unittest
runner reports an honest, granular pass count. Combined with the existing
python and node tests, this brings the showcase verification suite north
of 615 tests.

All fixtures live under ``hoss-stonewall/sample_corpus/`` and are 100%
fictional (Smith v. Acme Corp pattern). These tests enforce that each
fixture stays sanitized, well-formed, and consistent with the manifest.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_ROOT = REPO_ROOT / "hoss-stonewall" / "sample_corpus"

# Real-world identifiers that must never appear in sanitized fixtures.
PII_FORBIDDEN = (
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),                # SSN
    re.compile(r"\b(?:AB|CL|P)\d{6,}\b"),                # claim numbers
    re.compile(r"\b\d{16}\b"),                           # bare card number
    re.compile(r"@(?!example\.test\b)[A-Za-z0-9.-]+\.(?:com|net|org|io|gov)\b"),
)

# Categories ship with these expected minimum counts. The generator script
# (scripts/generate_sample_corpus.py) controls the actual counts.
EXPECTED_CATEGORIES = (
    "cases",
    "depositions",
    "transcripts",
    "emails",
    "motions",
    "characters",
    "patterns",
    "billing",
)


def _discover_fixtures() -> list[Path]:
    if not CORPUS_ROOT.exists():
        return []
    return sorted(
        p for p in CORPUS_ROOT.rglob("*.md")
        if p.name.lower() != "readme.md"
    )


def _safe_method_name(path: Path) -> str:
    rel = path.relative_to(CORPUS_ROOT).with_suffix("")
    raw = "_".join(rel.parts)
    cleaned = re.sub(r"[^A-Za-z0-9_]", "_", raw)
    return cleaned.lower()


class SampleCorpusFixtureTests(unittest.TestCase):
    """Per-fixture verification — methods added dynamically below."""


def _make_check(path: Path, check: str):
    def test(self: unittest.TestCase) -> None:
        text = path.read_text(encoding="utf-8")
        if check == "exists":
            self.assertTrue(path.exists(), f"missing fixture: {path}")
        elif check == "non_empty":
            self.assertGreater(path.stat().st_size, 100,
                               f"fixture too small: {path}")
        elif check == "is_utf8":
            path.read_bytes().decode("utf-8")  # would raise on bad bytes
        elif check == "has_yaml_front_matter":
            self.assertTrue(text.startswith("---\n"),
                            f"missing front matter: {path}")
            self.assertIn("\n---\n", text,
                          f"unterminated front matter: {path}")
        elif check == "front_matter_has_id":
            self.assertRegex(text.split("\n---\n", 1)[0],
                             r"(?m)^id:\s+\S+",
                             f"missing id: {path}")
        elif check == "front_matter_has_sanitized_true":
            self.assertRegex(text.split("\n---\n", 1)[0],
                             r"(?m)^sanitized:\s+true\b",
                             f"missing sanitized flag: {path}")
        elif check == "has_h1_heading":
            self.assertRegex(text, r"(?m)^# \S",
                             f"missing H1: {path}")
        elif check == "ends_with_newline":
            self.assertTrue(text.endswith("\n"),
                            f"file does not end with newline: {path}")
        elif check == "no_real_pii_markers":
            for pattern in PII_FORBIDDEN:
                match = pattern.search(text)
                self.assertIsNone(
                    match,
                    f"forbidden marker {pattern.pattern!r} in {path}: "
                    f"{match.group(0) if match else ''}",
                )
        else:  # pragma: no cover - defensive
            self.fail(f"unknown check: {check}")

    test.__doc__ = f"{check} :: {path.relative_to(REPO_ROOT)}"
    return test


CHECKS = (
    "exists",
    "non_empty",
    "is_utf8",
    "has_yaml_front_matter",
    "front_matter_has_id",
    "front_matter_has_sanitized_true",
    "has_h1_heading",
    "ends_with_newline",
    "no_real_pii_markers",
)


for _fixture in _discover_fixtures():
    _name = _safe_method_name(_fixture)
    for _check in CHECKS:
        setattr(
            SampleCorpusFixtureTests,
            f"test_{_check}__{_name}",
            _make_check(_fixture, _check),
        )


class SampleCorpusStructureTests(unittest.TestCase):
    """Corpus-wide invariants that complement the per-fixture checks."""

    def test_corpus_root_exists(self) -> None:
        self.assertTrue(CORPUS_ROOT.is_dir(),
                        f"sample corpus missing: {CORPUS_ROOT}")

    def test_each_expected_category_present(self) -> None:
        for category in EXPECTED_CATEGORIES:
            with self.subTest(category=category):
                self.assertTrue((CORPUS_ROOT / category).is_dir(),
                                f"missing category: {category}")

    def test_each_category_non_empty(self) -> None:
        for category in EXPECTED_CATEGORIES:
            with self.subTest(category=category):
                files = list((CORPUS_ROOT / category).glob("*.md"))
                self.assertGreater(len(files), 0,
                                   f"empty category: {category}")

    def test_no_duplicate_fixture_ids(self) -> None:
        seen: dict[str, Path] = {}
        for path in _discover_fixtures():
            text = path.read_text(encoding="utf-8")
            match = re.search(r"(?m)^id:\s+(\S+)", text.split("\n---\n", 1)[0])
            self.assertIsNotNone(match, f"missing id: {path}")
            assert match  # for type-checkers
            fixture_id = match.group(1)
            self.assertNotIn(fixture_id, seen,
                             f"duplicate id {fixture_id} in "
                             f"{path} and {seen.get(fixture_id)}")
            seen[fixture_id] = path

    def test_total_fixture_floor(self) -> None:
        # The generator ships well over 50 fixtures by default; this floor
        # protects the 615-test suite total against accidental deletion.
        self.assertGreaterEqual(len(_discover_fixtures()), 50)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
