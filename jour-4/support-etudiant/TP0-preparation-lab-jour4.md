# TP0 — Préparation du lab Jour 4

## Objectif

Préparer l’environnement d’audit automatisé et de code review.

## Étape 1 — Démarrer le lab

```bash
cd jour-4/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d --build
./check-lab.sh
```

## Étape 2 — Vérifier les URLs

Ouvrir :

```text
http://localhost:9000
http://localhost:5002/health
http://localhost:3002/health
```

## Étape 3 — Créer le dossier livrables

```bash
mkdir -p livrables
cp ../livrables-templates/00-validation-lab-jour4.md livrables/00-validation-lab-jour4.md
```

## Point d’attention

SonarQube peut prendre 1 à 3 minutes à démarrer.
Si l’interface ne répond pas immédiatement, attendre puis relancer `./check-lab.sh`.
