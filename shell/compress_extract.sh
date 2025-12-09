#!/usr/bin/env bash
# compress_extract: Compress and extract archives.
# Usage:
#   compress_extract.sh compress <output.tar.gz> <path1> [path2...]
#   compress_extract.sh extract <archive> [destination]
set -euo pipefail

mode=${1:-}
if [[ -z "$mode" || $mode == "-h" || $mode == "--help" ]]; then
  echo "Usage: $0 compress <output.tar.gz> <path1> [path2...] | extract <archive> [destination]" >&2
  exit 1
fi
shift

case "$mode" in
  compress)
    if [[ $# -lt 2 ]]; then
      echo "compress mode requires output archive and at least one path" >&2
      exit 1
    fi
    archive="$1"; shift
    tar -czf "$archive" "$@"
    echo "Created archive: $archive"
    ;;
  extract)
    if [[ $# -lt 1 ]]; then
      echo "extract mode requires an archive" >&2
      exit 1
    fi
    archive="$1"; dest="${2:-.}"
    mkdir -p "$dest"
    tar -xzf "$archive" -C "$dest"
    echo "Extracted $archive to $dest"
    ;;
  *)
    echo "Unknown mode: $mode" >&2
    exit 1
    ;;
 esac
