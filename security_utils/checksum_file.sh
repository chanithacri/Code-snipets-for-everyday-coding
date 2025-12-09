#!/usr/bin/env bash
# checksum_file: Compute and verify checksums.
# Usage: checksum_file.sh <file> [expected_checksum]
set -euo pipefail

FILE=${1:-}
EXPECTED=${2:-}

if [[ -z "$FILE" || $FILE == "-h" || $FILE == "--help" ]]; then
  echo "Usage: $0 <file> [expected_checksum]" >&2
  exit 1
fi

if [[ ! -f "$FILE" ]]; then
  echo "File not found: $FILE" >&2
  exit 1
fi

SUM=$(sha256sum "$FILE" | awk '{print $1}')

if [[ -z "$EXPECTED" ]]; then
  echo "$SUM  $FILE"
  exit 0
fi

if [[ "$SUM" == "$EXPECTED" ]]; then
  echo "Checksum OK"
  exit 0
else
  echo "Checksum mismatch" >&2
  exit 2
fi
