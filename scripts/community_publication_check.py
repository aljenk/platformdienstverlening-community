#!/usr/bin/env python3
"""Validate community publication docs for required content and obvious leakage.

The check is intentionally conservative. It validates the community-facing docs,
not the full internal evidence archive.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "community"
REQUIRED_FILES = [
    "README.md",
    "platformdienstverlening-community-publicatieplan.md",
    "bestuurlijke-samenvatting.md",
    "referentiearchitectuur.md",
    "technische-handleiding.md",
    "validatie-en-bewijs.md",
    "lessons-learned.md",
    "presentatie-outline.md",
    "publicatie-review-checklist.md",
    "community-post.md",
    "distributieplan.md",
    "begrippenlijst.md",
    "persona-review-2026-05-21.md",
    "reviewverzoeken.md",
    "feedback-register.md",
    "publicatie-index.md",
    "release-notes-communitybundel-2026-05-21.md",
    "demo-draaiboek-zonder-tweede-server.md",
    "demo-uitvoering-2026-05-21.md",
    "publicatie-readiness-2026-05-21.md",
    "publicatiepakket-manifest.md",
    "kanaalteksten-reviewpublicatie.md",
    "go-no-go-publicatiechecklist.md",
    "go-no-go-beoordeling-2026-05-21.md",
    "review-pr-body-2026-05-21.md",
]
REQUIRED_TERMS = [
    "11 out of 15 checks passed",
    "Haven+",
    "geen meerdere availability zones",
    "geen 3 masters",
    "geen 3 workers",
    "geen log aggregation",
]
FORBIDDEN_PATTERNS = [
    ("em_dash", re.compile("—")),
    ("internal_lan_ip", re.compile(r"\b192\.168\.\d+\.\d+\b")),
    ("kampman_domain", re.compile(r"kampman", re.IGNORECASE)),
    ("taxonic_name", re.compile(r"taxonic", re.IGNORECASE)),
    ("email_address", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
]


def main() -> int:
    failures: list[str] = []
    combined = ""
    for rel in REQUIRED_FILES:
        path = DOCS / rel
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"missing_or_empty file={path}")
            continue
        text = path.read_text()
        combined += "\n" + text
        for name, pattern in FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                failures.append(f"forbidden pattern={name} file={path} line={line}")
    for term in REQUIRED_TERMS:
        if term not in combined:
            failures.append(f"missing_required_term term={term!r}")
    status = "FAIL" if failures else "PASS"
    print(f"COMMUNITY_PUBLICATION_CHECK status={status} files={len(REQUIRED_FILES)}")
    for failure in failures:
        print(f"FAIL {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
