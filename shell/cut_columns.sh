#!/usr/bin/env bash
# cut_columns: Extract CSV columns with cut/awk.
# Usage: cut_columns.sh <file> <columns> [delimiter]
set -euo pipefail

FILE=${1:-}
COLUMNS=${2:-}
DELIM=${3:-,}

if [[ -z "$FILE" || -z "$COLUMNS" || $FILE == "-h" || $FILE == "--help" ]]; then
  echo "Usage: $0 <file> <columns> [delimiter]" >&2
  exit 1
fi

if [[ ! -f "$FILE" ]]; then
  echo "File not found: $FILE" >&2
  exit 1
fi

cut -d "$DELIM" -f "$COLUMNS" "$FILE"
