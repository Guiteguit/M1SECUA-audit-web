# J2-C02 — Stored XSS avec DVWA

## Objectif
Prouver qu’un payload XSS est stocké puis réexécuté après rechargement.

## Cible autorisée
`DVWA > Vulnerabilities > XSS Stored`

## Consignes
1. Régler DVWA en `Low`.
2. Envoyer un message normal.
3. Envoyer le payload suivant dans le message :
```html
<img src=x onerror=alert(1)>
```
4. Recharger la page.
5. Observer la requête POST dans Burp.

## Preuve attendue
Popup JavaScript, persistance après rechargement, endpoint, méthode, paramètre vulnérable, impact, remédiation.
