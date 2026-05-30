# TP5 — Fingerprinting technologique

Durée : 45 min

## Contexte

Le fingerprinting consiste à identifier les technologies utilisées par une application ou un service web.

Cette étape aide à orienter les tests, mais elle doit être interprétée avec prudence : les bannières peuvent être incomplètes, masquées ou volontairement trompeuses.

## Objectif

Identifier les technologies, versions probables et headers de sécurité exposés par :

```text
http://dvwa.target.local:8081
http://docs.target.local:8082
```

Vous devez distinguer :

- preuve directe ;
- indice faible ;
- hypothèse ;
- risque potentiel ;
- test de confirmation.

## Travail demandé

### 1. Relever les headers HTTP

```bash
curl -I http://dvwa.target.local:8081
curl -I http://docs.target.local:8082
```

À relever :

- `Server` ;
- `X-Powered-By` ;
- `Set-Cookie` ;
- redirections ;
- codes HTTP ;
- headers de sécurité présents ou absents.

### 2. Chercher les headers de sécurité

```bash
curl -I http://dvwa.target.local:8081 | grep -Ei "content-security-policy|x-frame-options|x-content-type-options|strict-transport-security|referrer-policy"
```

Répétez pour le portail documentaire :

```bash
curl -I http://docs.target.local:8082 | grep -Ei "content-security-policy|x-frame-options|x-content-type-options|strict-transport-security|referrer-policy"
```

Si la commande ne retourne rien, cela signifie que les headers recherchés ne sont probablement pas présents dans la réponse testée.

### 3. Utiliser WhatWeb

```bash
whatweb http://dvwa.target.local:8081
whatweb http://docs.target.local:8082
```

Pour chaque résultat, notez :

- technologie détectée ;
- version si disponible ;
- source de l'indice ;
- niveau de confiance ;
- intérêt pour l'audit.

### 4. Recouper avec Burp

Dans Burp :

```text
Proxy > HTTP history
```

Comparez les informations vues avec `curl` et `whatweb` :

- mêmes headers ?
- cookies identiques ?
- réponse différente après authentification ?
- headers différents selon les chemins ?

### 5. Qualifier l'impact potentiel

Pour chaque technologie ou header absent, formulez une hypothèse prudente :

```text
Observation : absence de X-Frame-Options.
Risque potentiel : clickjacking possible.
Limite : il faut vérifier le contexte applicatif et les pages réellement sensibles.
Test futur : contrôle dans un navigateur ou outil adapté.
```

Ne transformez pas automatiquement une absence de header en vulnérabilité critique.

## Headers à connaître

```text
Content-Security-Policy    Réduit certains risques XSS et injections de contenu
X-Frame-Options            Réduit le risque de clickjacking
X-Content-Type-Options     Limite le MIME sniffing
Strict-Transport-Security  Force HTTPS côté navigateur
Referrer-Policy            Contrôle les informations envoyées dans le Referer
```

Dans ce lab, les services sont en HTTP local. Certains headers comme HSTS n'ont pas le même sens que sur une application HTTPS réelle, mais il est utile de savoir les identifier.

## Livrable

Créez le fichier :

```bash
cp ../livrables-templates/05-fingerprinting.md livrables/05-fingerprinting.md
```

Complétez avec :

- technologies détectées ;
- headers importants ;
- headers de sécurité présents ou absents ;
- niveau de confiance ;
- interprétation courte pour chaque élément.

## Questions

1. Pourquoi un header `Server` peut-il être trompeur ?
2. Pourquoi faut-il recouper les résultats de `curl`, `whatweb` et Burp ?
3. Pourquoi l'absence d'un header de sécurité n'est-elle pas toujours une vulnérabilité critique ?
4. Quel header vous semble le plus important à vérifier sur une application exposée en production ?
