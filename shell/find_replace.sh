#!/usr/bin/env bash
# find_replace: Find and replace text recursively.
# Usage: find_replace.sh <pattern> <replacement> [path]
set -euo pipefail

PATTERN=${1:-}
REPLACEMENT=${2:-}
TARGET=${3:-.}

if [[ -z "$PATTERN" || -z "$REPLACEMENT" || $PATTERN == "-h" || $PATTERN == "--help" ]]; then
  echo "Usage: $0 <pattern> <replacement> [path]" >&2
  exit 1
fi

if command -v rg >/dev/null 2>&1; then
  rg --files-with-matches "$PATTERN" "$TARGET" | while read -r file; do
    perl -0777 -pi -e "s/$PATTERN/$REPLACEMENT/g" "$file"
    echo "Updated $file"
  done
else
  grep -R -l "$PATTERN" "$TARGET" | while read -r file; do
    sed -i "s/$PATTERN/$REPLACEMENT/g" "$file"
    echo "Updated $file"
  done
fi
