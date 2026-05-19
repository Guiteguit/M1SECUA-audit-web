#!/usr/bin/env bash
set -euo pipefail

echo "[+] Installation des paquets utiles pour le Jour 1"
sudo apt update
sudo apt install -y docker.io curl whatweb nmap ffuf nikto git nano tree zip

echo "[+] Activation de Docker"
sudo systemctl enable docker
sudo systemctl start docker

echo "[+] Ajout de l'utilisateur courant au groupe docker si nécessaire"
if ! groups "$USER" | grep -q docker; then
  sudo usermod -aG docker "$USER"
  echo "[!] Déconnectez/reconnectez-vous ou redémarrez pour utiliser docker sans sudo."
fi

echo "[+] Configuration des noms locaux dans /etc/hosts"
if ! grep -q "M1SECUA Jour 1 lab" /etc/hosts; then
  cat <<'EOF' | sudo tee -a /etc/hosts >/dev/null

# M1SECUA Jour 1 lab
127.0.0.1 target.local
127.0.0.1 www.target.local
127.0.0.1 dvwa.target.local
127.0.0.1 docs.target.local
127.0.0.1 admin.target.local
127.0.0.1 api.target.local
127.0.0.1 staging.target.local
127.0.0.1 dev.target.local
127.0.0.1 jenkins.target.local
127.0.0.1 grafana.target.local
127.0.0.1 internal.target.local
EOF
else
  echo "[=] Bloc hosts déjà présent."
fi

getent hosts dvwa.target.local
getent hosts docs.target.local

echo "[OK] Préparation terminée. Lancez : docker compose up -d"
