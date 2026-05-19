#!/usr/bin/env bash
set -euo pipefail

echo "[+] Conteneurs"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo
echo "[+] Tests HTTP"
for url in   http://localhost:9000   http://localhost:5002/health   http://localhost:3002/health
do
  echo "---- $url"
  curl -I --max-time 8 "$url" || true
done

echo
echo "[+] Outils"
source .venv-security/bin/activate
bandit --version || true
pip-audit --version || true
deactivate
node --version || true
npm --version || true
