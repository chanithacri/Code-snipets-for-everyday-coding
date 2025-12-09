#!/usr/bin/env bash
# ssl_cert_check: Check SSL certificate expiration.
# Usage: ssl_cert_check.sh <host> [port]
set -euo pipefail

HOST=${1:-}
PORT=${2:-443}

if [[ -z "$HOST" || $HOST == "-h" || $HOST == "--help" ]]; then
  echo "Usage: $0 <host> [port]" >&2
  exit 1
fi

EXPIRY=$(echo | openssl s_client -servername "$HOST" -connect "$HOST":"$PORT" 2>/dev/null \
  | openssl x509 -noout -enddate | cut -d= -f2)

if [[ -z "$EXPIRY" ]]; then
  echo "Unable to retrieve certificate for $HOST:$PORT" >&2
  exit 1
fi

echo "Certificate expires on: $EXPIRY"

after_seconds=$(( $(date --date="$EXPIRY" +%s) - $(date +%s) ))
days_left=$(( after_seconds / 86400 ))
if (( days_left < 0 )); then
  echo "Status: expired" >&2
  exit 2
elif (( days_left < 30 )); then
  echo "Status: expiring soon (${days_left}d)"
else
  echo "Status: valid (${days_left}d remaining)"
fi
