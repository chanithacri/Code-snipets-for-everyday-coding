#!/usr/bin/env bash
# largest_files: List largest files/folders.
# Usage: largest_files.sh [path] [count]
set -euo pipefail

TARGET="${1:-.}"
COUNT="${2:-10}"

if [[ ${TARGET} == "-h" || ${TARGET} == "--help" ]]; then
  echo "Usage: $0 [path] [count]" >&2
  exit 0
fi

du -ah "$TARGET" 2>/dev/null | sort -hr | head -n "$COUNT"
