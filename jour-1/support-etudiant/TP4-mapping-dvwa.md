# TP4 — Mapping applicatif DVWA

## Objectif
Cartographier DVWA avec Burp.

## Étapes
1. Ouvrir `http://dvwa.target.local:8081`.
2. Si besoin : `Create / Reset Database`.
3. Login : `admin / password`.
4. Mettre `DVWA Security` sur `Low`.
5. Naviguer dans tous les modules.
6. Relever endpoints, méthodes, paramètres, cookies.
7. Envoyer 3 requêtes dans Repeater.

## Endpoints à chercher
`/login.php`, `/security.php`, `/vulnerabilities/sqli/`, `/vulnerabilities/xss_r/`, `/vulnerabilities/exec/`, `/vulnerabilities/upload/`, `/vulnerabilities/fi/`.

## Livrable
```bash
cp ../livrables-templates/04-mapping-dvwa.md livrables/04-mapping-dvwa.md
```
