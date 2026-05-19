# TP0 — Préparation du rapport

## Objectif

Préparer l’espace de travail pour rédiger le rapport final.

## Étape 1 — Aller dans le lab Jour 5

```bash
cd jour-5/lab
chmod +x scripts/*.sh
```

## Étape 2 — Vérifier les outils

```bash
./scripts/check-tools.sh
```

## Étape 3 — Initialiser les livrables

```bash
./scripts/init-report.sh
```

## Étape 4 — Lire les findings d’exemple

```bash
cat findings/findings-jours1-4-sample.json | jq
```

## Étape 5 — Générer une synthèse automatique

```bash
./scripts/summarize-findings.py
```

## Livrable

Compléter :

```text
livrables/00-preparation-rapport.md
```
