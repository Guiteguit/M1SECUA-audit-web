# TP4 — SSRF avec Vuln API

## Objectif
Comprendre qu’une SSRF force le serveur à faire une requête.

Tester :
```bash
curl "http://vulnapi.target.local:5000/download?url=http://internal-admin"
curl "http://vulnapi.target.local:5000/download?url=http://127.0.0.1:5000/health"
```

Preuve attendue : `SSRF_INTERNAL_ACCESS_OK`.

## Remédiation attendue
Allowlist stricte, blocage IP privées/loopback/metadata, filtrage egress, proxy sortant, journalisation.

## Livrable
```bash
cp ../livrables-templates/04-ssrf.md livrables/04-ssrf.md
```
