# TP0 — Préparation du lab Jour 3

## Objectif

Démarrer le lab local pour les tests d’authentification et d’autorisation.

## Étape 1 — Démarrer

```bash
cd jour-3/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d --build
./check-lab.sh
```

## Étape 2 — Vérifier

Ouvrir :

```text
http://authapi.target.local:5001
http://dvwa.target.local:8081
http://webgoat.target.local:8080/WebGoat
http://juice.target.local:3000
```

## Étape 3 — Créer le dossier livrables

```bash
mkdir -p livrables
cp ../livrables-templates/00-validation-lab-jour3.md livrables/00-validation-lab-jour3.md
```
