# TP5 — Fingerprinting technologique

## Objectif
Identifier les technologies et headers de sécurité.

## Commandes
```bash
curl -I http://dvwa.target.local:8081
curl -I http://docs.target.local:8082
whatweb http://dvwa.target.local:8081
whatweb http://docs.target.local:8082
curl -I http://dvwa.target.local:8081 | grep -Ei "content-security-policy|x-frame-options|x-content-type-options|strict-transport-security|referrer-policy"
```

## Livrable
```bash
cp ../livrables-templates/05-fingerprinting.md livrables/05-fingerprinting.md
```
