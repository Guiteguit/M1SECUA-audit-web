# TP1 — Reconnaissance passive locale

Durée : 45 min

## Contexte

Vous réalisez la première phase d'un audit web : la reconnaissance passive.

Dans une mission réelle, cette phase consiste à collecter des informations publiques sans interagir directement avec la cible technique. Dans ce lab, les sources OSINT sont simulées localement pour rester dans un cadre légal et contrôlé.

## Objectif

Identifier les informations exposées qui peuvent orienter la suite de l'audit :

- sous-domaines ;
- documents publics ;
- technologies probables ;
- endpoints oubliés ;
- identifiants de test ;
- hypothèses de risque ;
- URLs à explorer avec Burp.

## Périmètre autorisé

Vous devez utiliser uniquement :

```text
jour-1/lab/osint-evidence/
http://docs.target.local:8082
```

Ne faites pas de recherche Internet réelle sur une entreprise, une école ou un domaine public.

## Travail demandé

### 1. Se placer dans le dossier du lab

```bash
cd jour-1/lab
```

### 2. Lire les sources OSINT simulées

```bash
cat osint-evidence/google-results.txt
cat osint-evidence/crtsh-results.txt
cat osint-evidence/whois-result.txt
cat osint-evidence/dns-records.txt
cat osint-evidence/shodan-result.txt
```

Pour chaque source, notez :

- ce que la source prétend révéler ;
- le niveau de confiance ;
- l'intérêt pour un audit ;
- les pistes à vérifier plus tard.

### 3. Explorer le portail documentaire

Ouvrez dans le navigateur :

```text
http://docs.target.local:8082
```

Vous pouvez aussi lister les fichiers publics côté lab :

```bash
find osint-public -maxdepth 2 -type f -print
```

L'objectif n'est pas d'exploiter une vulnérabilité, mais de repérer les informations qui n'auraient pas dû être publiées.

### 4. Construire une première cartographie

Relevez les éléments suivants :

- noms d'hôtes ou sous-domaines ;
- chemins ou endpoints mentionnés ;
- comptes, emails ou identifiants de test ;
- technologies et versions ;
- indices d'environnement interne ;
- informations d'architecture ;
- pages à tester avec Burp dans les prochains TP.

### 5. Qualifier les risques

Pour chaque information intéressante, posez-vous trois questions :

```text
Qu'est-ce que cette information révèle ?
Comment un attaquant pourrait-il s'en servir ?
Comment vérifier ce risque sans sortir du périmètre ?
```

Exemples de qualification :

```text
Sous-domaine admin -> surface sensible -> vérifier s'il existe dans le lab
Version applicative -> risque de CVE -> vérifier la technologie sans exploiter Internet
Identifiant de test -> risque d'accès non autorisé -> tester uniquement si le TP l'autorise
```

## Points d'attention

- Une information trouvée en OSINT n'est pas automatiquement une vulnérabilité.
- Une hypothèse doit être vérifiée avant d'apparaître comme finding.
- La reconnaissance passive prépare la reconnaissance active, elle ne la remplace pas.
- Le niveau de confiance doit être documenté : source directe, trace ancienne, indice faible, etc.

## Livrable

Créez le fichier :

```bash
cp ../livrables-templates/01-reconnaissance-passive.md livrables/01-reconnaissance-passive.md
```

Complétez au minimum :

- 5 URLs ou chemins intéressants ;
- 5 sous-domaines ou noms d'hôtes ;
- les documents exposés les plus sensibles ;
- 5 hypothèses de risque à vérifier dans les prochains TP.

## Questions

1. Quelle différence faites-vous entre reconnaissance passive et reconnaissance active ?
2. Pourquoi une information publique peut-elle quand même représenter un risque ?
3. Pourquoi faut-il indiquer le niveau de confiance d'une information OSINT ?
4. Donnez un exemple d'hypothèse qui devra être vérifiée avec Burp.
