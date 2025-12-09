#!/usr/bin/env bash
# monitor_resources: Monitor CPU/memory usage.
# Prints quick system stats and top processes.
set -euo pipefail

if [[ ${1:-} == "-h" || ${1:-} == "--help" ]]; then
  echo "Usage: $0" >&2
  exit 0
fi

echo "== Host: $(hostname) =="
echo "Uptime: $(uptime -p)"
echo "Load : $(cut -d ' ' -f1-3 /proc/loadavg)"
echo

echo "== Memory =="
free -h

echo

echo "== Disk usage =="
df -h / | awk 'NR==1 || NR==2 {print}'

echo

echo "== Top CPU consumers =="
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6

echo

echo "== Top memory consumers =="
ps -eo pid,comm,%cpu,%mem --sort=-%mem | head -n 6
