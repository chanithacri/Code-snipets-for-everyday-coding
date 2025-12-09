#!/usr/bin/env bash
# download_file: Download with curl/wget.
# Usage: download_file.sh <url> [output_path]
set -euo pipefail

URL=${1:-}
OUTPUT=${2:-}

if [[ -z "$URL" || $URL == "-h" || $URL == "--help" ]]; then
  echo "Usage: $0 <url> [output_path]" >&2
  exit 1
fi

if command -v curl >/dev/null 2>&1; then
  if [[ -n "$OUTPUT" ]]; then
    curl -fsSL "$URL" -o "$OUTPUT"
  else
    curl -fsSL "$URL"
  fi
elif command -v wget >/dev/null 2>&1; then
  if [[ -n "$OUTPUT" ]]; then
    wget -O "$OUTPUT" "$URL"
  else
    wget "$URL"
  fi
else
  echo "Neither curl nor wget is available." >&2
  exit 1
fi
