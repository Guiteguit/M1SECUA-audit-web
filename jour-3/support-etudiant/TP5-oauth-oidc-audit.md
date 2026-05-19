# TP5 — Audit OAuth 2.0 / OpenID Connect

## Objectif

Comprendre les erreurs classiques d’implémentation OAuth/OIDC.

Ce TP utilise une simulation locale volontairement faible.

## Test 1 — Authorization request normale

```bash
curl -i "http://authapi.target.local:5001/oauth/authorize?client_id=labapp&redirect_uri=http://authapi.target.local:5001/callback&state=abc123"
```

Observer le header `Location`.

## Test 2 — Redirect URI non maîtrisée

```bash
curl -i "http://authapi.target.local:5001/oauth/authorize?client_id=labapp&redirect_uri=http://evil.local/callback&state=abc123"
```

Question :

Le serveur accepte-t-il une redirect_uri arbitraire ?

## Test 3 — State absent

```bash
curl -i "http://authapi.target.local:5001/oauth/authorize?client_id=labapp&redirect_uri=http://authapi.target.local:5001/callback"
```

Question :

Le paramètre `state` est-il obligatoire ?

## À documenter

- redirect URI validation ;
- présence ou absence de state ;
- risque de vol de code ;
- recommandations.

## Remédiation attendue

- whitelist stricte des redirect_uri ;
- state obligatoire et imprévisible ;
- PKCE pour clients publics ;
- tokens jamais exposés dans des logs ou URLs non maîtrisées ;
- scopes minimaux.

## Livrable

```bash
cp ../livrables-templates/05-oauth-oidc.md livrables/05-oauth-oidc.md
```
