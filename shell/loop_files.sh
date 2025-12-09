#!/usr/bin/env bash
# loop_files: Loop through files in a directory.
# Usage: loop_files.sh <path> [glob]
set -euo pipefail

TARGET=${1:-.}
GLOB=${2:-*}

if [[ $TARGET == "-h" || $TARGET == "--help" ]]; then
  echo "Usage: $0 <path> [glob]" >&2
  exit 0
fi

shopt -s nullglob
for file in "$TARGET"/$GLOB; do
  [[ -f "$file" ]] || continue
  echo "$file"
done
