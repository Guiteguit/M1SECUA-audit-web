# TP1 — Audit d’authentification

## Objectif

Tester un mécanisme d’authentification faible et vérifier la présence ou l’absence de protections.

## Partie A — Login normal

Tester un login valide :

```bash
curl -i -X POST http://authapi.target.local:5001/login \
  -d "username=alice&password=alice123"
```

Observer :

- code HTTP ;
- cookie `LABSESSID` ;
- flags du cookie ;
- message de réponse.

## Partie B — Login invalide

```bash
curl -i -X POST http://authapi.target.local:5001/login \
  -d "username=alice&password=wrong"
```

Observer :

- code HTTP ;
- message d’erreur ;
- différence entre succès et échec.

## Partie C — Test de dictionnaire limité

Utiliser uniquement la petite wordlist du lab.

```bash
while read pwd; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -X POST http://authapi.target.local:5001/login \
    -d "username=admin&password=$pwd")
  echo "$pwd -> $code"
done < wordlists/passwords-small.txt
```

## À documenter

- y a-t-il du rate limiting ?
- y a-t-il un lockout compte ?
- les messages d’erreur sont-ils trop précis ?
- le cookie est-il protégé ?
- quelles recommandations proposer ?

## Livrable

```bash
cp ../livrables-templates/01-authentification.md livrables/01-authentification.md
```
