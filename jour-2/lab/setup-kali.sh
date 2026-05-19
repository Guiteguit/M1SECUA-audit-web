#!/usr/bin/env bash
set -euo pipefail
sudo apt update
sudo apt install -y docker.io docker-compose-plugin curl nmap ffuf nikto whatweb jq python3 python3-pip git nano tree
sudo systemctl enable docker
sudo systemctl start docker
if ! groups "$USER" | grep -q docker; then
  sudo usermod -aG docker "$USER"
  echo "[!] Déconnectez/reconnectez-vous ou redémarrez pour utiliser Docker sans sudo."
fi
HOSTS_BLOCK="
# M1SECUA Jour 2 lab
127.0.0.1 dvwa.target.local
127.0.0.1 juice.target.local
127.0.0.1 webgoat.target.local
127.0.0.1 vulnapi.target.local
127.0.0.1 internal.target.local
"
if ! grep -q "M1SECUA Jour 2 lab" /etc/hosts; then
  echo "$HOSTS_BLOCK" | sudo tee -a /etc/hosts >/dev/null
fi
echo "[OK] Préparation terminée. Lancez : docker compose up -d --build"
