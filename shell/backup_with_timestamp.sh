#!/usr/bin/env bash
# backup_with_timestamp: Backup a directory with timestamp.
# Usage: backup_with_timestamp.sh <source_dir> [destination_dir]
# Creates a compressed tarball named <source>_YYYYmmdd_HHMMSS.tar.gz in destination_dir.
set -euo pipefail

if [[ ${1:-} == "-h" || ${1:-} == "--help" || $# -lt 1 ]]; then
  echo "Usage: $0 <source_dir> [destination_dir]" >&2
  exit 1
fi

SRC_DIR="$1"
DEST_DIR="${2:-backups}"
if [[ ! -d "$SRC_DIR" ]]; then
  echo "Source directory not found: $SRC_DIR" >&2
  exit 1
fi

mkdir -p "$DEST_DIR"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
ARCHIVE_NAME="$(basename "$SRC_DIR")_${TIMESTAMP}.tar.gz"
ARCHIVE_PATH="$(realpath "$DEST_DIR")/$ARCHIVE_NAME"

tar -czf "$ARCHIVE_PATH" -C "$(dirname "$SRC_DIR")" "$(basename "$SRC_DIR")"
echo "Backup created at $ARCHIVE_PATH"
