# J3-C05 — OAuth redirect_uri et state

## Objectif
Identifier deux erreurs OAuth/OIDC : redirect_uri libre et state optionnel.

## Tests
```bash
curl -i "http://authapi.target.local:5001/oauth/authorize?client_id=labapp&redirect_uri=http://authapi.target.local:5001/callback&state=abc123"

curl -i "http://authapi.target.local:5001/oauth/authorize?client_id=labapp&redirect_uri=http://evil.local/callback&state=abc123"

curl -i "http://authapi.target.local:5001/oauth/authorize?client_id=labapp&redirect_uri=http://authapi.target.local:5001/callback"
```

## Preuve attendue
Header `Location`, redirect_uri arbitraire acceptée, state optionnel, risque, remédiation : redirect_uri préenregistrée, state obligatoire, PKCE.
