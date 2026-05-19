#!/usr/bin/env bash
set -euo pipefail

docker compose down -v
docker compose up -d --build
echo "[OK] Lab Jour 3 réinitialisé."
