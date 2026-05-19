# TP5 — Désérialisation non sécurisée

## Objet simple
```bash
python3 - << 'PY'
import pickle, base64
payload = base64.b64encode(pickle.dumps({"user":"student","role":"user"})).decode()
print(payload)
PY
```

Puis :
```bash
curl "http://vulnapi.target.local:5000/deserialize?obj=COLLER_ICI"
```

Le danger est `pickle.loads()` sur une donnée non fiable.

## Livrable
```bash
cp ../livrables-templates/05-deserialisation.md livrables/05-deserialisation.md
```
