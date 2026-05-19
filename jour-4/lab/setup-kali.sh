#!/usr/bin/env bash
set -euo pipefail

echo "[+] Installation des outils Jour 4"
sudo apt update
sudo apt install -y docker.io curl jq python3 python3-pip python3-venv git nano tree nodejs npm

echo "[+] Installation de Bandit et pip-audit dans un venv local"
python3 -m venv .venv-security
source .venv-security/bin/activate
pip install --upgrade pip
pip install bandit pip-audit
deactivate

echo "[+] Installation ESLint côté lab JS"
if [ -d sample-js-app ]; then
  cd sample-js-app
  npm install || true
  cd ..
fi

echo "[+] Activation Docker"
sudo systemctl enable docker
sudo systemctl start docker

if ! groups "$USER" | grep -q docker; then
  sudo usermod -aG docker "$USER"
  echo "[!] Votre utilisateur a été ajouté au groupe docker."
  echo "[!] Déconnectez/reconnectez-vous ou redémarrez avant de continuer."
fi

echo "[OK] Préparation terminée."
echo "Lancez : docker compose up -d"
