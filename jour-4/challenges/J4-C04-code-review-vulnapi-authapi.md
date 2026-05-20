# J4-C04 — Code Review Vuln API / Auth API

## Objectif
Identifier des patterns dangereux dans le code des applications maison.

## Patterns à chercher
```text
pickle.loads
resolve_entities=True
requests.get(url utilisateur)
alg=none
role modifiable par l’utilisateur
redirect_uri non validée
absence de token CSRF
absence de contrôle propriétaire
```

## Commande utile
```bash
grep -R "pickle\|resolve_entities\|requests.get\|alg\|role\|redirect_uri\|csrf" jour-2 jour-3
```

## Preuve attendue
Fichier, fonction, pattern, risque, remédiation pour 5 findings minimum.
