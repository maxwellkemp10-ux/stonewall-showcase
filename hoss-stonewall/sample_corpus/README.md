# Sample Corpus

This directory ships **78 fictional fixtures** that demonstrate the shape of
the Stonewall corpus without exposing any real matter, witness, claim
number, or carrier.

Every file follows the **Smith v. Acme Corp** convention required by the
project's security rules. Every file carries `sanitized: true` in its YAML
front matter and is verified on every push by the parameterized test suite
in [`tests/test_sample_corpus.py`](../../tests/test_sample_corpus.py).

## Categories

| Directory       | Count | What it represents                                            |
|-----------------|-------|---------------------------------------------------------------|
| `cases/`        | 12    | Matter postures, key dates, pattern tags                      |
| `depositions/`  | 10    | Witness outline templates                                     |
| `transcripts/`  | 8     | Status-conference transcript fragments                        |
| `emails/`       | 14    | Sanitized counsel-to-counsel correspondence                   |
| `motions/`      | 10    | Motion-to-compel templates                                    |
| `characters/`   | 10    | Composite role cards (adjuster, expert, witness, etc.)        |
| `patterns/`     | 8     | Phenomenology pattern definitions                             |
| `billing/`      | 6     | Sample line-item billing tables                               |

## Verification

Each fixture is exercised by **9 checks**:

1. `exists`
2. `non_empty`
3. `is_utf8`
4. `has_yaml_front_matter`
5. `front_matter_has_id`
6. `front_matter_has_sanitized_true`
7. `has_h1_heading`
8. `ends_with_newline`
9. `no_real_pii_markers` (rejects SSNs, claim-number patterns, bare card
   numbers, and any non-`example.test` email domain)

That produces **702 per-fixture tests + 5 corpus-wide invariant tests =
707 tests** in this module alone, contributing to the showcase's 615+
test verification suite.

## Regenerating

The fixtures are deterministic. To regenerate them after editing the
generator:

```bash
python3 scripts/generate_sample_corpus.py
```

## Sanitization Rules

- All party names are drawn from a fixed list of generic surnames and
  fictional corporate placeholders (e.g., `Acme Corp`, `Globex Logistics`,
  `Initech Freight`).
- All email addresses use the `example.test` reserved TLD.
- No real claim numbers, policy numbers, addresses, or phone numbers
  appear anywhere in this directory.
