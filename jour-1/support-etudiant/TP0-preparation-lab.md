# TP0 — Préparation du lab Kali

## Objectif
Préparer Kali, Docker, les outils et les noms locaux.

## Commandes
```bash
cd jour-1/lab
chmod +x setup-kali.sh check-lab.sh
./setup-kali.sh
docker compose up -d
./check-lab.sh
```

## Livrable
```bash
mkdir -p livrables
cp ../livrables-templates/00-validation-lab.md livrables/00-validation-lab.md
```
Complétez le fichier avec les résultats de `docker ps` et `curl -I`.
