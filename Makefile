.PHONY: bootstrap smoke test-node test-python verify repo-sweep brief-help ingest-help

bootstrap:
	./scripts/bootstrap_env.sh

smoke:
	./scripts/surface_smoke.sh

test-node:
	node --test tests/qb1_tracker_helpers.test.mjs tests/email_consolidator.test.mjs

test-python:
	python3 -m unittest tests.test_ingest_onedrive tests.test_verify_repo_consistency tests.test_tactical_brief tests.test_legal_matters_offline_backfill

verify:
	python3 scripts/verify_repo_consistency.py

repo-sweep:
	python3 scripts/repo_sweep.py

brief-help:
	python3 scripts/tactical_brief.py --help

ingest-help:
	python3 scripts/ingest_onedrive.py --help
