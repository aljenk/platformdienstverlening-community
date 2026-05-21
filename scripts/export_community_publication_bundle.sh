#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT"

STAMP=${1:-$(date -u +%Y%m%dT%H%M%SZ)}
OUT_DIR="dist/community-publication-$STAMP"
BUNDLE="dist/platformdienstverlening-community-publication-$STAMP.tar.gz"
CHECKSUMS="dist/platformdienstverlening-community-publication-$STAMP.sha256"
MANIFEST="docs/community/publicatiepakket-manifest.md"

FILES=(
  docs/community/publicatie-index.md
  docs/community/community-post.md
  docs/community/release-notes-communitybundel-2026-05-21.md
  docs/community/publicatie-readiness-2026-05-21.md
  docs/community/bestuurlijke-samenvatting.md
  docs/community/referentiearchitectuur.md
  docs/community/technische-handleiding.md
  docs/community/begrippenlijst.md
  docs/community/validatie-en-bewijs.md
  docs/community/demo-draaiboek-zonder-tweede-server.md
  docs/community/demo-uitvoering-2026-05-21.md
  docs/community/lessons-learned.md
  docs/community/presentatie-outline.md
  docs/community/publicatie-review-checklist.md
  docs/community/persona-review-2026-05-21.md
  docs/community/reviewverzoeken.md
  docs/community/feedback-register.md
  docs/community/distributieplan.md
  docs/community/publicatiepakket-manifest.md
  scripts/community_publication_check.py
  .github/ISSUE_TEMPLATE/community-feedback.yml
)

scripts/community_publication_check.py >/tmp/community_publication_check_export.log
rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

for file in "${FILES[@]}"; do
  test -s "$file"
  mkdir -p "$OUT_DIR/$(dirname "$file")"
  cp "$file" "$OUT_DIR/$file"
done

find "$OUT_DIR" -type f -print | sort | while read -r file; do
  rel=${file#"$OUT_DIR"/}
  sha256sum "$file" | awk -v rel="$rel" '{print $1 "  " rel}'
done > "$OUT_DIR/SHA256SUMS"

mkdir -p dist
tar -C dist -czf "$BUNDLE" "community-publication-$STAMP"
sha256sum "$BUNDLE" > "$CHECKSUMS"

printf 'COMMUNITY_PUBLICATION_BUNDLE status=PASS files=%s out=%s checksums=%s\n' "${#FILES[@]}" "$BUNDLE" "$CHECKSUMS"
