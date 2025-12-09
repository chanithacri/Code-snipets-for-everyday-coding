#!/usr/bin/env bash
# check_network: Check network connectivity.
# Performs DNS lookup and a simple HTTP request.
set -euo pipefail

HOST="${1:-example.com}"

if [[ $HOST == "-h" || $HOST == "--help" ]]; then
  echo "Usage: $0 [host]" >&2
  exit 0
fi

echo "Checking DNS for $HOST"
if getent hosts "$HOST" >/dev/null; then
  echo "DNS resolution: ok"
else
  echo "DNS resolution failed for $HOST" >&2
  exit 1
fi

echo "Pinging $HOST"
if ping -c 1 -W 2 "$HOST" >/dev/null 2>&1; then
  echo "Ping: ok"
else
  echo "Ping failed (may be blocked)"
fi

echo "HTTP GET https://$HOST"
if command -v curl >/dev/null 2>&1; then
  curl -I --max-time 5 "https://$HOST" | head -n 1
else
  echo "curl not installed" >&2
fi
