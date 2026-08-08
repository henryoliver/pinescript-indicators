#!/usr/bin/env bash
# Mirror the shared block-trade engine from the source-of-truth indicator into the
# companion panel. Edit the logic ONLY in the source file, between the <<SYNC …>>
# markers, then run this. Each named region's body (the lines strictly between its
# BEGIN and END markers) is copied verbatim; the marker lines themselves are left
# alone in each file, so their trailing notes can differ.
#
#   Usage:  scripts/sync-block-engine.sh          # apply the sync
#           scripts/sync-block-engine.sh --check  # verify in sync, change nothing (CI / pre-commit)
#
# Exit codes: 0 = success / in sync · 1 = usage or marker error · 2 = --check found drift.
set -euo pipefail

cd "$(dirname "$0")/.."

SRC="ticker-tape.pine"
DST="ticker-block-trades.pine"
REGIONS=(block-cond block-classify)

CHECK=0
[ "${1:-}" = "--check" ] && CHECK=1

for f in "$SRC" "$DST"; do
    [ -f "$f" ] || { echo "✗ missing file: $f" >&2; exit 1; }
done

# Extract the body strictly between BEGIN/END markers for one region in one file.
extract() {
    awk -v r="$1" '
        $0 ~ ("<<SYNC " r " BEGIN>>") { inblk = 1; next }
        $0 ~ ("<<SYNC " r " END>>")   { inblk = 0 }
        inblk { print }
    ' "$2"
}

# Replace that region body in DST with SRC's, keeping DST's own marker lines.
replace() {
    local region="$1" bodyfile="$2" file="$3"
    awk -v r="$region" -v bf="$bodyfile" '
        $0 ~ ("<<SYNC " r " BEGIN>>") { print; while ((getline line < bf) > 0) print line; skip = 1; next }
        $0 ~ ("<<SYNC " r " END>>")   { skip = 0 }
        !skip { print }
    ' "$file"
}

changed=0
work="$(mktemp)"; cp "$DST" "$work"

for region in "${REGIONS[@]}"; do
    for f in "$SRC" "$DST"; do
        grep -q "<<SYNC ${region} BEGIN>>" "$f" && grep -q "<<SYNC ${region} END>>" "$f" \
            || { echo "✗ region '${region}' markers missing in $f" >&2; rm -f "$work"; exit 1; }
    done
    body="$(mktemp)"; extract "$region" "$SRC" > "$body"
    out="$(mktemp)";  replace "$region" "$body" "$work" > "$out"; mv "$out" "$work"
    rm -f "$body"
done

if cmp -s "$work" "$DST"; then
    echo "✓ ${DST} already in sync with ${SRC}"
    rm -f "$work"
    exit 0
fi

changed=1
if [ "$CHECK" -eq 1 ]; then
    echo "✗ ${DST} is OUT OF SYNC with ${SRC} — run scripts/sync-block-engine.sh" >&2
    rm -f "$work"
    exit 2
fi

mv "$work" "$DST"
echo "✓ synced block engine → ${DST}"
