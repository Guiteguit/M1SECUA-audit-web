# TP0 — Préparation du lab Jour 2

## Objectif
Démarrer DVWA, Juice Shop, WebGoat, Vuln API et Internal Admin.

## Étapes
```bash
cd jour-2/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d --build
./check-lab.sh
```

Ouvrir :
- http://dvwa.target.local:8081
- http://juice.target.local:3000
- http://webgoat.target.local:8080/WebGoat
- http://vulnapi.target.local:5000
- http://internal.target.local:8088

Initialiser DVWA si besoin : `Create / Reset Database`, login `admin / password`, sécurité `Low`.

## Livrable
```bash
mkdir -p livrables
cp ../livrables-templates/00-validation-lab-jour2.md livrables/00-validation-lab-jour2.md
```
