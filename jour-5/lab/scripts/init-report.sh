#!/usr/bin/env bash
set -euo pipefail

mkdir -p livrables
cp -n ../livrables-templates/*.md livrables/ || true
cp -n templates/rapport-final-template.md livrables/rapport-final.md
cp -n templates/slides-restitution-template.md livrables/slides-restitution.md

echo "[OK] Templates copiés dans lab/livrables/"
ls -la livrables
