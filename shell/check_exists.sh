#!/usr/bin/env bash
# check_exists: Check if file/folder exists.
# Usage: check_exists.sh <path>
set -euo pipefail

if [[ ${1:-} == "-h" || ${1:-} == "--help" || $# -ne 1 ]]; then
  echo "Usage: $0 <path>" >&2
  exit 1
fi

TARGET="$1"
if [[ -e "$TARGET" ]]; then
  if [[ -d "$TARGET" ]]; then
    echo "Directory exists: $TARGET"
  else
    echo "File exists: $TARGET"
  fi
  exit 0
else
  echo "Not found: $TARGET" >&2
  exit 2
fi
