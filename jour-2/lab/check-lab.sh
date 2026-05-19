#!/usr/bin/env bash
set -euo pipefail
docker ps --format "table {{.Names}}	{{.Status}}	{{.Ports}}"
for url in   http://dvwa.target.local:8081   http://juice.target.local:3000   http://webgoat.target.local:8080/WebGoat   http://vulnapi.target.local:5000/health   http://internal.target.local:8088
do
  echo "---- $url"
  curl -I --max-time 8 "$url" || true
done
