# Publication sur GitHub

## Recommandation
Créer deux dépôts :

1. `M1SECUA-audit-web` public : supports étudiants + lab.
2. `M1SECUA-audit-web-corrections` privé : corrections, barème détaillé, notes formateur.

## Commandes de publication

```bash
git init
git add .
git commit -m "Initialisation Jour 1 - lab audit web"
git branch -M main
git remote add origin https://github.com/<ORG_OU_USER>/M1SECUA-audit-web.git
git push -u origin main
```

## Commandes étudiants

```bash
git clone https://github.com/<ORG_OU_USER>/M1SECUA-audit-web.git
cd M1SECUA-audit-web/jour-1/lab
chmod +x setup-kali.sh check-lab.sh
./setup-kali.sh
docker compose up -d
./check-lab.sh
```
