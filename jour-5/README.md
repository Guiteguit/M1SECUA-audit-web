# Jour 5 — Rapport d’Audit et Remédiation

## Objectifs pédagogiques

À la fin du Jour 5, vous devez être capables de :

- structurer un rapport d’audit professionnel ;
- rédiger un Executive Summary compréhensible par le management ;
- décrire un finding technique complet ;
- classifier les risques avec une approche CVSS ;
- prioriser les remédiations ;
- proposer des recommandations de secure coding ;
- préparer une présentation de restitution ;
- communiquer différemment selon l’audience : management, développeurs, sécurité.

## Cadre légal et confidentialité

Les rapports produits pendant ce TP concernent uniquement le lab pédagogique.

Interdictions :

- intégrer des données personnelles réelles ;
- intégrer des captures provenant d’un système externe ;
- publier le rapport sur un dépôt public avec des secrets, tokens ou informations nominatives ;
- réutiliser les PoC sur un environnement non autorisé.

## Démarrage rapide

```bash
cd jour-5/lab
chmod +x scripts/*.sh
./scripts/check-tools.sh
./scripts/init-report.sh
```

## Déroulé des TP

1. `TP0-preparation-rapport.md`
2. `TP1-executive-summary.md`
3. `TP2-findings-techniques.md`
4. `TP3-cvss-priorisation.md`
5. `TP4-plan-remediation.md`
6. `TP5-secure-coding.md`
7. `TP6-presentation-stakeholders.md`
8. `TP7-synthese-finale.md`

## Livrables attendus

```text
livrables/
├── 00-preparation-rapport.md
├── 01-executive-summary.md
├── 02-findings-techniques.md
├── 03-cvss-priorisation.md
├── 04-plan-remediation.md
├── 05-secure-coding.md
├── 06-presentation-stakeholders.md
├── 07-synthese-finale.md
├── rapport-final.md
└── slides-restitution.md
```

## Message important

Un bon rapport n’est pas une liste de failles.

Un bon rapport permet de décider :

```text
Qu’est-ce qui est vulnérable ?
Quel est le risque réel ?
Qui est impacté ?
Que faut-il corriger ?
Dans quel ordre ?
Comment vérifier que c’est corrigé ?
```
