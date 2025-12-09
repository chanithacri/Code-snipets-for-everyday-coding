#!/usr/bin/env bash
# ssh_keys: Generate and use SSH keys.
set -euo pipefail

KEY_NAME=${KEY_NAME:-id_ed25519}
KEY_PATH="$HOME/.ssh/$KEY_NAME"
EMAIL=${EMAIL:-dev@example.com}

mkdir -p "$HOME/.ssh"
if [ ! -f "$KEY_PATH" ]; then
  ssh-keygen -t ed25519 -C "$EMAIL" -f "$KEY_PATH" -N ""
else
  echo "Key already exists at $KEY_PATH"
fi

# Ensure correct permissions
chmod 700 "$HOME/.ssh"
chmod 600 "$KEY_PATH"
chmod 644 "$KEY_PATH.pub"

# Add to ssh-agent if available
if command -v ssh-agent >/dev/null 2>&1; then
  eval "$(ssh-agent -s)"
  ssh-add "$KEY_PATH"
fi

echo "Public key (add to GitHub/GitLab/servers):"
cat "$KEY_PATH.pub"
