#!/usr/bin/env bash
set -euo pipefail

echo "[+] Vérification des outils utiles"
for cmd in python3 jq git zip; do
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "[OK] $cmd"
  else
    echo "[KO] $cmd manquant"
  fi
done

if command -v pandoc >/dev/null 2>&1; then
  echo "[OK] pandoc disponible"
else
  echo "[INFO] pandoc non installé. Conversion PDF optionnelle."
fi
