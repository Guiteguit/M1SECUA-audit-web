#!/usr/bin/env bash
set -euo pipefail

echo "[+] Installation des outils Jour 3"
sudo apt update
sudo apt install -y docker.io docker-compose-plugin curl jq python3 python3-pip git nano tree

echo "[+] Activation Docker"
sudo systemctl enable docker
sudo systemctl start docker

if ! groups "$USER" | grep -q docker; then
  sudo usermod -aG docker "$USER"
  echo "[!] Votre utilisateur a été ajouté au groupe docker."
  echo "[!] Déconnectez/reconnectez-vous ou redémarrez avant de continuer."
fi

echo "[+] Configuration /etc/hosts"
HOSTS_BLOCK="
# M1SECUA Jour 3 lab
127.0.0.1 dvwa.target.local
127.0.0.1 webgoat.target.local
127.0.0.1 juice.target.local
127.0.0.1 authapi.target.local
"

if ! grep -q "M1SECUA Jour 3 lab" /etc/hosts; then
  echo "$HOSTS_BLOCK" | sudo tee -a /etc/hosts >/dev/null
else
  echo "[=] Bloc hosts Jour 3 déjà présent."
fi

echo "[OK] Préparation terminée."
echo "Lancez : docker compose up -d --build"
