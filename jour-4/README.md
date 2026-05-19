# Jour 4 — Audit automatisé et Code Review

## Objectifs pédagogiques

À la fin du Jour 4, vous devez être capables de :

- différencier SAST, DAST et IAST ;
- lancer une analyse statique Python avec Bandit ;
- lancer une analyse JavaScript avec ESLint Security ;
- démarrer SonarQube localement ;
- analyser un projet de code avec SonarQube ;
- conduire une code review sécurité manuelle ;
- identifier les faux positifs ;
- proposer des remédiations réalistes ;
- préparer une intégration DevSecOps dans un pipeline CI/CD.

## Cadre légal

Les manipulations sont strictement limitées aux projets de code fournis dans ce dépôt et aux conteneurs locaux.

Cibles autorisées :

- code source dans `jour-4/lab/sample-python-app`
- code source dans `jour-4/lab/sample-js-app`
- SonarQube local `http://localhost:9000`
- applications locales démarrées par Docker

Interdictions :

- scanner du code privé non autorisé ;
- pousser des secrets réels dans GitHub ;
- lancer des scans sur des applications externes ;
- publier des résultats contenant des données sensibles.

## Démarrage rapide

```bash
cd jour-4/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d
./check-lab.sh
```

## Déroulé des TP

1. `TP0-preparation-lab-jour4.md`
2. `TP1-bandit-python-sast.md`
3. `TP2-eslint-security-js.md`
4. `TP3-sonarqube-local.md`
5. `TP4-code-review-manuelle.md`
6. `TP5-devsecops-pipeline.md`
7. `TP6-synthese-jour4.md`

## Livrables attendus

```text
livrables/
├── 00-validation-lab-jour4.md
├── 01-bandit-python.md
├── 02-eslint-security.md
├── 03-sonarqube.md
├── 04-code-review-manuelle.md
├── 05-devsecops-pipeline.md
└── 06-synthese-jour4.md
```

## Message important

Un outil SAST ne remplace pas une analyse humaine.

Le bon réflexe professionnel :

```text
Détection automatique → validation humaine → impact → remédiation → preuve de correction
```
