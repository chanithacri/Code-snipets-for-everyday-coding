#!/usr/bin/env bash
# kill_by_name: Kill process by name safely.
# Usage: kill_by_name.sh <pattern> [signal]
set -euo pipefail

PATTERN=${1:-}
SIGNAL=${2:-TERM}

if [[ -z "$PATTERN" || $PATTERN == "-h" || $PATTERN == "--help" ]]; then
  echo "Usage: $0 <pattern> [signal]" >&2
  exit 1
fi

PIDS=$(pgrep -f "$PATTERN" || true)
if [[ -z "$PIDS" ]]; then
  echo "No processes found matching: $PATTERN" >&2
  exit 1
fi

echo "Killing processes:"
pgrep -fl "$PATTERN"
kill -s "$SIGNAL" $PIDS
