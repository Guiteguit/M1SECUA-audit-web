# TP4 — Mapping applicatif DVWA

Durée : 1h

## Contexte

Vous avez configuré Burp. Vous allez maintenant cartographier l'application DVWA comme lors d'un début d'audit applicatif.

Le mapping consiste à comprendre :

- les pages disponibles ;
- les fonctionnalités ;
- les paramètres ;
- les méthodes HTTP ;
- les cookies ;
- les zones authentifiées ;
- les futures surfaces de test.

## Objectif

Produire une cartographie exploitable de DVWA pour préparer les tests des jours suivants.

À la fin du TP, vous devez avoir identifié les endpoints importants et les paramètres qui pourront être testés plus tard pour SQL injection, XSS, command injection, upload, file inclusion ou problèmes de session.

## Périmètre autorisé

Autorisé :

```text
http://dvwa.target.local:8081
```

N'effectuez pas encore d'exploitation agressive. Aujourd'hui, l'objectif est l'observation et la cartographie.

## Travail demandé

### 1. Ouvrir DVWA

Dans Firefox configuré avec Burp :

```text
http://dvwa.target.local:8081
```

Si DVWA n'est pas initialisé, utilisez :

```text
Create / Reset Database
```

### 2. Se connecter

Identifiants du lab :

```text
admin / password
```

Ces identifiants sont fictifs et uniquement destinés au laboratoire.

### 3. Configurer le niveau de sécurité

Dans DVWA :

```text
DVWA Security -> Low
```

Ce niveau permet d'observer des comportements volontairement vulnérables. Il ne représente pas une configuration acceptable en production.

### 4. Naviguer méthodiquement

Avec Burp ouvert, parcourez les modules DVWA :

```text
SQL Injection
XSS reflected
Command Injection
File Upload
File Inclusion
CSRF
Brute Force
```

Pour chaque module, notez :

- URL ;
- méthode HTTP ;
- paramètres ;
- présence de cookie ;
- formulaire ou action utilisateur ;
- risque potentiel ;
- priorité de test pour les jours suivants.

### 5. Relever les endpoints importants

Endpoints à retrouver :

```text
/login.php
/security.php
/vulnerabilities/sqli/
/vulnerabilities/xss_r/
/vulnerabilities/exec/
/vulnerabilities/upload/
/vulnerabilities/fi/
```

Vous pouvez en relever d'autres si vous les observez dans Burp.

### 6. Analyser les cookies et la session

Dans Burp, observez les headers `Cookie` et `Set-Cookie`.

Relevez :

- nom des cookies ;
- rôle supposé ;
- présence d'un cookie de session ;
- changement après login ;
- lien éventuel avec le niveau de sécurité DVWA.

Ne modifiez pas encore les cookies : vous documentez seulement.

### 7. Envoyer trois requêtes dans Repeater

Choisissez trois requêtes intéressantes :

```text
Une requête de login ou session
Une requête avec paramètre GET
Une requête avec paramètre POST ou upload
```

Envoyez-les dans Repeater et observez :

- ce qui change si vous renvoyez la requête ;
- les paramètres visibles ;
- le code HTTP ;
- la réponse HTML ;
- les indices de validation côté serveur.

### 8. Construire une matrice de test

Pour chaque endpoint important, préparez une ligne de ce type :

```text
Endpoint -> Paramètre -> Type de saisie -> Risque possible -> Test futur
```

Exemple :

```text
/vulnerabilities/sqli/ -> id -> GET -> injection SQL possible -> test Jour 2
```

## Erreurs fréquentes à éviter

- Cliquer partout sans documenter.
- Confondre endpoint observé et vulnérabilité prouvée.
- Oublier les cookies.
- Ne regarder que les pages visibles et ignorer les requêtes dans Burp.
- Tester des payloads agressifs avant d'avoir cartographié l'application.

## Livrable

Créez le fichier :

```bash
cp ../livrables-templates/04-mapping-dvwa.md livrables/04-mapping-dvwa.md
```

Complétez avec :

- liste des endpoints ;
- méthodes HTTP ;
- paramètres ;
- cookies observés ;
- trois requêtes envoyées dans Repeater ;
- matrice de tests à prévoir pour le jour 2.

## Questions

1. Pourquoi cartographier une application avant de tester des payloads ?
2. Quelle différence faites-vous entre une page, un endpoint et un paramètre ?
3. Pourquoi les cookies sont-ils importants dans un audit web ?
4. Quel endpoint DVWA vous semble prioritaire pour le jour 2, et pourquoi ?
