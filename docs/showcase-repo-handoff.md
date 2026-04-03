# Stonewall Showcase — Repository Handoff Runbook

This document describes how to safely export sanitized content from the private
`Stonewall` repository into the public `stonewall-showcase` repository.

## Principles

1. **No PII or case data** — strip all client names, claim numbers, lore, and
   internal identifiers before anything reaches `stonewall-showcase`.
2. **No credentials** — never copy `.env`, tokens, or database IDs.
3. **Preserve architecture** — the showcase should reflect the full automation
   pipeline and system design without exposing production data.

## Workflow A — File-Only Copy (Recommended)

The safest approach: copy individual files and commit with a clean message.

```bash
# 1. Clone the showcase repo
git clone https://github.com/maxwellkemp10-ux/stonewall-showcase.git
cd stonewall-showcase
git checkout -b showcase-update

# 2. Copy sanitized files from your local Stonewall clone
#    Replace <STONEWALL_PATH> with your local Stonewall repo path
cp <STONEWALL_PATH>/docs/showcase.html docs/
cp <STONEWALL_PATH>/scripts/new_script.py scripts/

# 3. Review the diff for any PII or credentials
git diff

# 4. Stage and commit with a clean message
git add docs/ scripts/
git commit -m "Import sanitized updates from Stonewall v9"

# 5. Push and open a PR
git push -u origin showcase-update
```

## Workflow B — Cherry-Pick (Preserves Authorship)

Use `--no-commit` to avoid leaking private commit messages into public history.

```bash
# 1. Clone the showcase repo
git clone https://github.com/maxwellkemp10-ux/stonewall-showcase.git
cd stonewall-showcase
git checkout -b showcase-update

# 2. Add the private repo as a remote
git remote add stonewall-src <STONEWALL_PATH>
git fetch stonewall-src

# 3. Cherry-pick WITHOUT committing (to avoid leaking private commit messages)
git cherry-pick --no-commit <STONEWALL_COMMIT_HASH>

# 4. Scope to showcase-safe files only — unstage anything sensitive
git reset HEAD catalog/ sources/ .env
git checkout -- catalog/ sources/ .env 2>/dev/null

# 5. Review the staged diff for PII
git diff --cached

# 6. Commit with a clean, sanitized message
git commit -m "Import sanitized Stonewall v9 showcase page"

# 7. Push and open a PR
git push -u origin showcase-update
```

## Guardrails

| Rule | Detail |
|------|--------|
| **Branch naming** | Use `showcase-*` prefix for all showcase update branches |
| **File scope** | Only export from `docs/`, `scripts/`, `tests/`, `.github/`, `.claude/`, `agents/` |
| **Never export** | `sources/`, `catalog/`, `.env`, `*.local.json`, batch output files |
| **Review before push** | Always run `git diff` and search for client names, claim numbers, and internal references |
| **Test after import** | Run `python -m unittest discover tests/` in the showcase repo to verify nothing broke |

## Verification Checklist

- [ ] No `.env` or credential files in the diff
- [ ] No client names, claim numbers, or case-specific data
- [ ] No internal lore or personal identifiers
- [ ] All Notion database IDs use placeholder values
- [ ] OneDrive paths use environment variable references, not hardcoded paths
- [ ] Tests pass in the showcase repo
- [ ] Commit messages are clean and don't reference private work
