# TP2 — Sessions et CSRF

## Objectif

Analyser les cookies de session et tester une action sensible sans token CSRF.

## Partie A — Récupérer un cookie de session

```bash
curl -i -c cookies.txt -X POST http://authapi.target.local:5001/login \
  -d "username=alice&password=alice123"
```

Puis :

```bash
cat cookies.txt
```

## Partie B — Appeler /me avec le cookie

```bash
curl -b cookies.txt http://authapi.target.local:5001/me | jq
```

## Partie C — Tester une action sensible

```bash
curl -b cookies.txt -X POST http://authapi.target.local:5001/transfer \
  -d "to=bob&amount=100" | jq
```

## Analyse

L’action `/transfer` est sensible. Elle devrait être protégée par un token CSRF.

Questions :

1. Le serveur demande-t-il un token CSRF ?
2. L’action est-elle possible avec uniquement le cookie de session ?
3. Quels flags de cookie sont présents ?
4. Que recommander ?

## Livrable

```bash
cp ../livrables-templates/02-sessions-csrf.md livrables/02-sessions-csrf.md
```
