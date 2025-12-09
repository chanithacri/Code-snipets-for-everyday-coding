#!/usr/bin/env bash
# grep_search: Search inside files with grep (prefers ripgrep if available).
# Usage: grep_search.sh <pattern> [path]
set -euo pipefail

PATTERN=${1:-}
TARGET=${2:-.}

if [[ -z "$PATTERN" || $PATTERN == "-h" || $PATTERN == "--help" ]]; then
  echo "Usage: $0 <pattern> [path]" >&2
  exit 1
fi

if command -v rg >/dev/null 2>&1; then
  rg "$PATTERN" "$TARGET"
else
  grep -R --line-number --color=always "$PATTERN" "$TARGET"
fi
