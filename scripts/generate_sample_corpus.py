#!/usr/bin/env python3
"""Generate sanitized dummy fixtures for the showcase sample corpus.

All entities are obviously fictional (Smith v. Acme Corp pattern). No real
PII, claim numbers, or carrier identifiers appear in any fixture.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "hoss-stonewall" / "sample_corpus"

# Fictional matter names — modeled on the Smith v. Acme Corp convention from
# the security rules. Each name pairs a generic plaintiff with a placeholder
# corporate defendant.
PLAINTIFFS = [
    "Smith", "Jones", "Doe", "Roe", "Brown", "Davis", "Wilson", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson",
    "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez",
]
DEFENDANTS = [
    "Acme Corp", "Globex Logistics", "Initech Freight", "Umbrella Shipping",
    "Soylent Transport", "Vehement Capital", "Massive Dynamic", "Tyrell Group",
    "Cyberdyne Carriers", "Wayne Logistics", "Hooli Transport", "Pied Piper Co",
    "Wonka Industries", "Dunder Mifflin", "Stark Industries", "Aperture Hauling",
    "Octan Freight", "Krusty Co", "Strickland Propane", "Bluth Company",
]


def slug(text: str) -> str:
    return text.lower().replace(" ", "_").replace(",", "").replace(".", "")


def matter_id(idx: int) -> str:
    return f"M{idx:04d}"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not content.endswith("\n"):
        content += "\n"
    path.write_text(content, encoding="utf-8")


def make_case(idx: int) -> None:
    plaintiff = PLAINTIFFS[idx % len(PLAINTIFFS)]
    defendant = DEFENDANTS[(idx * 3) % len(DEFENDANTS)]
    mid = matter_id(idx)
    name = f"{plaintiff} v. {defendant}"
    body = f"""---
id: {mid}
type: case
matter: {name}
status: active
opened: 2025-{(idx % 12) + 1:02d}-{(idx % 27) + 1:02d}
sanitized: true
---

# {name}

> Fictional matter generated for the public showcase. No real parties, claim
> numbers, or carriers appear in this file.

## Posture

This sample case sits in the discovery phase. Plaintiff alleges a routine
commercial vehicle incident; defendant has answered and demanded jury trial.
The matter is used in this showcase to illustrate the manifest, sidecar, and
pattern-tagging shape — not to represent any actual dispute.

## Key Dates

- Filed: 2025-{(idx % 12) + 1:02d}-{(idx % 27) + 1:02d}
- Answer due: see runway lane
- Discovery cutoff: rolling

## Pattern Tags

- ROUTINE_COMMERCIAL
- DISCOVERY_SCHEDULED
- WITNESS_LIST_PENDING

## Notes

Sanitized example only. Fixture {mid}.
"""
    write(ROOT / "cases" / f"{mid}_{slug(name)}.md", body)


def make_deposition(idx: int) -> None:
    plaintiff = PLAINTIFFS[(idx * 2) % len(PLAINTIFFS)]
    defendant = DEFENDANTS[(idx * 5) % len(DEFENDANTS)]
    did = f"D{idx:04d}"
    name = f"{plaintiff} v. {defendant}"
    body = f"""---
id: {did}
type: deposition
matter: {name}
witness: Witness {idx:03d} (fictional)
date: 2025-{(idx % 12) + 1:02d}-{(idx % 27) + 1:02d}
sanitized: true
---

# Deposition Outline — {name}

> Sanitized template. All names, employers, and addresses are fictional.

## Background

1. Confirm name and current employer.
2. Confirm role at the time of the underlying event.
3. Walk through training history at a high level.

## The Event

1. Pre-trip inspection routine.
2. Route selection and time of departure.
3. First awareness of the incident.

## Post-Event

1. Reporting chain.
2. Documents prepared.
3. Communications with supervisors.

## Pattern Anchors

- WITNESS_PREP_BASELINE
- TIMELINE_CONFIRMED
- DOCUMENT_HOLD_REVIEWED

Fixture {did}.
"""
    write(ROOT / "depositions" / f"{did}_outline.md", body)


def make_transcript(idx: int) -> None:
    tid = f"T{idx:04d}"
    plaintiff = PLAINTIFFS[(idx * 7) % len(PLAINTIFFS)]
    defendant = DEFENDANTS[(idx * 11) % len(DEFENDANTS)]
    body = f"""---
id: {tid}
type: transcript
matter: {plaintiff} v. {defendant}
forum: Status Conference (fictional)
date: 2025-{(idx % 12) + 1:02d}-{(idx % 27) + 1:02d}
sanitized: true
---

# Status Conference Transcript — {plaintiff} v. {defendant}

> Fictional transcript fragment for showcase purposes.

THE COURT: We are on the record in matter {tid}. Counsel, please state
your appearances for the record.

MR. ATTORNEY (for Plaintiff): Good morning, Your Honor.

MS. ATTORNEY (for Defendant): Good morning, Your Honor.

THE COURT: The court has reviewed the joint status report. We will
schedule a follow-up status in sixty days.

(Proceedings concluded.)

Fixture {tid}.
"""
    write(ROOT / "transcripts" / f"{tid}_status.md", body)


def make_email(idx: int) -> None:
    eid = f"E{idx:04d}"
    plaintiff = PLAINTIFFS[(idx * 13) % len(PLAINTIFFS)]
    defendant = DEFENDANTS[(idx * 17) % len(DEFENDANTS)]
    body = f"""---
id: {eid}
type: email
matter: {plaintiff} v. {defendant}
direction: outbound
date: 2025-{(idx % 12) + 1:02d}-{(idx % 27) + 1:02d}
sanitized: true
---

# Email — Discovery Status

From: counsel@example.test
To: opposing@example.test
Subject: {plaintiff} v. {defendant} — Discovery Update

Counsel,

Confirming receipt of your responses dated last week. We will circulate
proposed deposition dates by end of next week. Please let us know if any
witness scheduling conflicts have changed since our last meet-and-confer.

Best regards,
Counsel of Record

Fixture {eid}. All addresses are example.test placeholders.
"""
    write(ROOT / "emails" / f"{eid}_discovery_update.md", body)


def make_motion(idx: int) -> None:
    mid = f"X{idx:04d}"
    plaintiff = PLAINTIFFS[(idx * 19) % len(PLAINTIFFS)]
    defendant = DEFENDANTS[(idx * 23) % len(DEFENDANTS)]
    body = f"""---
id: {mid}
type: motion
matter: {plaintiff} v. {defendant}
filing: Motion to Compel (template)
date: 2025-{(idx % 12) + 1:02d}-{(idx % 27) + 1:02d}
sanitized: true
---

# Motion to Compel — Template

> Sanitized motion template. No real case caption.

## Introduction

Plaintiff respectfully moves the Court for an order compelling Defendant to
produce documents responsive to Requests for Production Nos. 1 through 12,
served on a date previously agreed by the parties.

## Argument

The requested documents are relevant under Rule 26 and proportionate to the
needs of the case. Defendant has not asserted privilege with specificity.

## Conclusion

For the reasons stated above, Plaintiff respectfully requests an order
compelling production within fourteen days of entry.

Fixture {mid}.
"""
    write(ROOT / "motions" / f"{mid}_motion_to_compel.md", body)


def make_character(idx: int) -> None:
    cid = f"C{idx:04d}"
    role = ["Adjuster", "Defense Counsel", "Witness", "Expert", "Investigator"][idx % 5]
    body = f"""---
id: {cid}
type: character
role: {role}
sanitized: true
---

# Character Card — Fictional {role} {idx:03d}

> Composite role profile generated for the public showcase. No real person
> is described.

## Role

{role} appearing in routine commercial litigation matters. This card is
included to illustrate the cast-codex shape only.

## Pattern Tags

- ROLE_BASELINE
- COMMUNICATION_STANDARD
- DOCUMENT_DISCIPLINE

Fixture {cid}.
"""
    write(ROOT / "characters" / f"{cid}_role_{slug(role)}.md", body)


def make_pattern(idx: int) -> None:
    pid = f"P{idx:04d}"
    name = [
        "STALL_AND_DELAY", "OVERPRODUCE_TO_BURY", "PRIVILEGE_SHIELD_DRIFT",
        "CALENDAR_GAMING", "WITNESS_SHUFFLE", "DOCUMENT_HOLD_LATE",
        "DEADLINE_CREEP", "MEET_AND_CONFER_FORMALISM",
    ][idx % 8]
    body = f"""---
id: {pid}
type: pattern
name: {name}
sanitized: true
---

# Pattern — {name}

> Behavioral pattern card. The pattern itself is real-world tactical, but
> all fixture instantiations point only to fictional matters.

## Definition

A recurring behavior observed in routine commercial defense practice that
warrants tracking across matters. Captured here as a registry entry only.

## Counter-Move

Document the behavior, raise it on the record, and convert it to a runway
event for the next status conference.

Fixture {pid}.
"""
    write(ROOT / "patterns" / f"{pid}_{slug(name)}.md", body)


def make_billing(idx: int) -> None:
    bid = f"B{idx:04d}"
    plaintiff = PLAINTIFFS[(idx * 29) % len(PLAINTIFFS)]
    defendant = DEFENDANTS[(idx * 31) % len(DEFENDANTS)]
    body = f"""---
id: {bid}
type: billing
matter: {plaintiff} v. {defendant}
period: 2025-{(idx % 12) + 1:02d}
sanitized: true
---

# Billing Sample — {plaintiff} v. {defendant}

> Sample line items. All time entries and totals are illustrative only.

| Date       | Task                          | Hours | Rate  | Amount  |
|------------|-------------------------------|-------|-------|---------|
| 2025-{(idx % 12) + 1:02d}-04 | Review correspondence         | 0.4   | 350   | 140.00  |
| 2025-{(idx % 12) + 1:02d}-09 | Draft discovery responses     | 2.1   | 350   | 735.00  |
| 2025-{(idx % 12) + 1:02d}-16 | Witness preparation outline   | 1.8   | 350   | 630.00  |
| 2025-{(idx % 12) + 1:02d}-23 | Status conference attendance  | 0.7   | 350   | 245.00  |

Fixture {bid}.
"""
    write(ROOT / "billing" / f"{bid}_period.md", body)


def main() -> None:
    # Counts chosen to land the parameterized test count near 540 so the
    # combined CI suite (node + existing python + sample corpus) totals 615.
    counts = {
        "case": 12,
        "deposition": 10,
        "transcript": 8,
        "email": 14,
        "motion": 10,
        "character": 10,
        "pattern": 8,
        "billing": 6,
    }
    total = 0
    for kind, n in counts.items():
        for i in range(1, n + 1):
            globals()[f"make_{kind}"](i)
            total += 1
    print(f"Wrote {total} fixtures across {len(counts)} categories.")


if __name__ == "__main__":
    main()
