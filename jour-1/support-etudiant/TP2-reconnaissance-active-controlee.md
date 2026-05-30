# TP2 — Reconnaissance active contrôlée

Durée : 45 min à 1h

## Contexte

Après la reconnaissance passive, vous passez à une reconnaissance active limitée au lab.

La reconnaissance active consiste à envoyer des requêtes vers la cible pour confirmer :

- quels services répondent ;
- quelles technologies semblent utilisées ;
- quels chemins existent ;
- quels comportements HTTP sont observables.

## Objectif

Collecter des preuves techniques sur les deux services du jour 1 :

```text
http://dvwa.target.local:8081
http://docs.target.local:8082
```

À la fin du TP, vous devez produire une première vue technique exploitable pour la suite de l'audit.

## Périmètre autorisé

Autorisé :

```text
127.0.0.1
dvwa.target.local:8081
docs.target.local:8082
```

Interdit :

- scanner Internet ;
- scanner le réseau de l'école ;
- scanner la machine d'un autre étudiant ;
- utiliser des options agressives sans consigne ;
- lancer des scans sur des ports non demandés.

## Travail demandé

### 1. Vérifier que le lab est démarré

Depuis `jour-1/lab` :

```bash
docker ps
curl -I http://dvwa.target.local:8081
curl -I http://docs.target.local:8082
```

Si les services ne répondent pas, revenez au TP0.

### 2. Identifier les services exposés

Lancez un scan limité aux ports autorisés :

```bash
nmap -sV -p 8081,8082 127.0.0.1
```

À relever :

- port ;
- état ;
- service détecté ;
- version ou bannière si disponible ;
- limite de confiance de la détection.

Remarque : `nmap` donne des indications, pas une vérité absolue. Toute détection doit être recoupée avec d'autres preuves.

### 3. Observer les en-têtes HTTP

```bash
curl -I http://dvwa.target.local:8081
curl -I http://docs.target.local:8082
```

Relevez :

- code HTTP ;
- serveur annoncé ;
- cookies ;
- redirections ;
- headers de sécurité présents ou absents.

### 4. Identifier les technologies avec WhatWeb

```bash
whatweb http://dvwa.target.local:8081
whatweb http://docs.target.local:8082
```

Pour chaque technologie détectée, indiquez :

- la source de la preuve ;
- votre niveau de confiance ;
- l'intérêt pour l'audit.

### 5. Rechercher des chemins connus avec ffuf

```bash
ffuf -u http://dvwa.target.local:8081/FUZZ -w wordlists/wordlist-lab.txt -mc all
```

À relever :

- chemins trouvés ;
- codes HTTP ;
- tailles de réponse ;
- chemins à revisiter dans Burp.

Attention : dans un audit réel, le fuzzing doit être cadré. Il peut générer beaucoup de trafic, provoquer des alertes ou perturber une application fragile.

### 6. Croiser les résultats avec le TP1

Comparez les indices OSINT du TP1 avec les résultats actifs :

```text
Une URL mentionnée en OSINT existe-t-elle réellement ?
Un sous-domaine sensible répond-il ?
Une technologie annoncée est-elle confirmée ?
```

## Interprétation attendue

Un bon résultat ne se limite pas à une sortie de commande.

Pour chaque élément intéressant, vous devez expliquer :

```text
Observation -> Interprétation -> Risque potentiel -> Suite du test
```

Exemple :

```text
Observation : un endpoint /login.php répond.
Interprétation : une surface d'authentification existe.
Risque potentiel : brute-force, session faible, injection sur formulaire.
Suite du test : mapping Burp puis tests contrôlés Jour 2/Jour 3.
```

## Livrable

Créez le fichier :

```bash
cp ../livrables-templates/02-reconnaissance-active.md livrables/02-reconnaissance-active.md
```

Complétez :

- résultat `nmap` ;
- headers HTTP importants ;
- résultats `whatweb` ;
- chemins trouvés avec `ffuf` ;
- commentaires d'interprétation.

## Questions

1. Pourquoi limiter `nmap` aux ports `8081` et `8082` ?
2. Pourquoi un header `Server` ne doit-il pas être considéré comme une preuve suffisante ?
3. Quelle différence faites-vous entre découvrir un chemin et prouver une vulnérabilité ?
4. Pourquoi le fuzzing doit-il être maîtrisé dans un audit professionnel ?
