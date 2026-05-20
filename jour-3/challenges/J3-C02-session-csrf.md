# J3-C02 — Session et CSRF

## Objectif
Tester une action sensible sans token CSRF.

## Commandes
```bash
curl -i -c cookies.txt -X POST http://authapi.target.local:5001/login \
  -d "username=alice&password=alice123"

curl -b cookies.txt http://authapi.target.local:5001/me | jq

curl -b cookies.txt -X POST http://authapi.target.local:5001/transfer \
  -d "to=bob&amount=100" | jq
```

## DVWA
Observer le module CSRF de DVWA et identifier la requête sensible.

## Preuve attendue
Cookie, action sensible, absence de token CSRF, impact, remédiation.
