#!/usr/bin/env bash
set -euo pipefail

echo "[+] Vérification Docker"
docker ps

echo "
[+] Vérification HTTP DVWA"
curl -I --max-time 5 http://dvwa.target.local:8081 || true

echo "
[+] Vérification HTTP portail documentaire"
curl -I --max-time 5 http://docs.target.local:8082 || true

echo "
[+] URLs à ouvrir :"
echo "    http://dvwa.target.local:8081"
echo "    http://docs.target.local:8082"
