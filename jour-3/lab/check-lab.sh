#!/usr/bin/env bash
set -euo pipefail

echo "[+] Conteneurs"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo
echo "[+] Tests HTTP"
for url in   http://dvwa.target.local:8081   http://webgoat.target.local:8080/WebGoat   http://juice.target.local:3000   http://authapi.target.local:5001/health
do
  echo "---- $url"
  curl -I --max-time 8 "$url" || true
done

echo
echo "[+] URLs principales"
echo "DVWA      : http://dvwa.target.local:8081"
echo "WebGoat   : http://webgoat.target.local:8080/WebGoat"
echo "JuiceShop : http://juice.target.local:3000"
echo "Auth API  : http://authapi.target.local:5001"
