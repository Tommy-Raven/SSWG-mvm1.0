#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DRY_RUN=false
DOCTOR=false

case "${1:-}" in
  --dry-run) DRY_RUN=true ;;
  --doctor) DOCTOR=true; DRY_RUN=true ;;
  "") ;;
  *) echo "Unknown argument: $1"; exit 2 ;;
esac

log() { echo "▶ $*"; }
require() { command -v "$1" >/dev/null || { echo "❌ missing: $1"; exit 1; }; }

if $DOCTOR; then
  log "Doctor: sswg_mvm_1.0"

  require python3
  require pipx

  for tool in pytest ruff black pip-audit bandit; do
    if command -v "$tool" >/dev/null; then
      echo "✓ $tool"
    else
      echo "❌ missing $tool (run ~/github/pipx-bootstrap.sh)"
    fi
  done

  echo "✓ doctor complete"
  exit 0
fi

log "No setup actions required (tools managed via pipx)"
echo "✓ setup complete"
