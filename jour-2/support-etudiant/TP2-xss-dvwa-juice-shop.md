# TP2 — XSS avec DVWA et Juice Shop

## Objectif
Comprendre XSS reflected, stored et DOM.

## Reflected XSS
Dans DVWA : `Vulnerabilities > XSS Reflected`.

Tester :
```html
test
<img src=x onerror=alert(1)>
```

## Stored XSS — DVWA

### Objectif

Vérifier qu’un payload XSS peut être stocké côté serveur puis réexécuté après rechargement de la page.

### Étapes

1. Ouvrir DVWA : `http://dvwa.target.local:8081`
2. Se connecter avec `admin / password`.
3. Aller dans `DVWA Security` et choisir `Low`.
4. Aller dans `Vulnerabilities > XSS Stored`.
5. Envoyer un message normal.
6. Envoyer ensuite dans le champ Message :

```html
<img src=x onerror=alert(1)>
```
7. Recharger la page.
8. Vérifier si le payload se réexécute.
9. Observer la requête dans Burp HTTP history.
10. Documenter endpoint, méthode, paramètre, payload, preuve et impact.

## DOM — Observation avec Juice Shop

### Objectif

Comprendre comment une application moderne modifie dynamiquement le DOM côté navigateur.

### Étapes

1. Ouvrir `http://juice.target.local:3000`.
2. Ouvrir les DevTools avec F12.
3. Dans `Elements`, observer la structure DOM.
4. Dans `Console`, observer les erreurs ou messages.
5. Dans `Network`, Naviguer à travers les APIs affichés et essayer certains filtres.
6. Recharger la page et effectuer une recherche produit.
7. Identifier au moins un endpoint API appelé par le navigateur.
8. Dans `Sources`, rechercher des mots-clés comme `localStorage`, `token`, `innerHTML`, `eval`.
9. Documenter les observations.


## Livrable
```bash
cp ../livrables-templates/02-xss.md livrables/02-xss.md
```
