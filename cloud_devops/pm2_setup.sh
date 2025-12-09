#!/usr/bin/env bash
# pm2_setup: PM2 setup for Node.js.
set -euo pipefail

if ! command -v pm2 >/dev/null 2>&1; then
  echo "Installing pm2 globally..."
  npm install -g pm2
fi

APP_NAME=${APP_NAME:-app}
ENTRY=${ENTRY:-dist/index.js}

# Start app under pm2 and configure startup
pm2 start "$ENTRY" --name "$APP_NAME" --env production
pm2 save
pm2 startup systemd -u "$(whoami)" --hp "$HOME"

echo "PM2 status:"
pm2 status "$APP_NAME"
