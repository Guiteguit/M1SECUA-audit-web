#!/usr/bin/env bash
set -euo pipefail

NAME="${1:-NOM-PRENOM}"
zip -r "livrables-jour5-${NAME}.zip" livrables/
echo "[OK] Archive créée : livrables-jour5-${NAME}.zip"
