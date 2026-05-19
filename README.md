# M1SECUA — Sécurité Web Avancée et Audit

Dépôt pédagogique pour le module **Sécurité Web Avancée et Audit**.

## Objectif du dépôt

Ce dépôt contient les supports de TP et le laboratoire technique pour le **Jour 1 — Méthodologies d'audit et reconnaissance**.

## Cadre légal

Les manipulations sont strictement limitées aux environnements de laboratoire fournis dans ce dépôt.

Cibles autorisées pour le Jour 1 :

- `http://dvwa.target.local:8081`
- `http://docs.target.local:8082`
- `127.0.0.1`
- `target.local` et ses sous-domaines locaux

Interdictions :

- scanner ou tester un site public ;
- scanner le réseau de l'école ;
- scanner la machine d'un autre étudiant ;
- utiliser Burp, Nmap, ffuf, Nikto ou tout autre outil offensif hors du périmètre autorisé ;
- publier des résultats ou captures contenant des informations personnelles.

## Démarrage rapide Jour 1

```bash
git clone https://github.com/<ORG_OU_USER>/M1SECUA-audit-web.git
cd M1SECUA-audit-web/jour-1/lab
chmod +x setup-kali.sh check-lab.sh
./setup-kali.sh
docker compose up -d
./check-lab.sh
```

Puis suivre les TP dans l'ordre :

1. `jour-1/support-etudiant/TP0-preparation-lab.md`
2. `jour-1/support-etudiant/TP1-reconnaissance-passive-locale.md`
3. `jour-1/support-etudiant/TP2-reconnaissance-active-controlee.md`
4. `jour-1/support-etudiant/TP3-configuration-burp.md`
5. `jour-1/support-etudiant/TP4-mapping-dvwa.md`
6. `jour-1/support-etudiant/TP5-fingerprinting.md`
7. `jour-1/support-etudiant/TP6-synthese-jour1.md`

## Rendu attendu

Chaque étudiant ou binôme rend un fichier :

```text
livrables-jour1-NOM-PRENOM.zip
```

Contenant :

```text
livrables/
├── 00-validation-lab.md
├── 01-reconnaissance-passive.md
├── 02-reconnaissance-active.md
├── 03-configuration-burp.md
├── 04-mapping-dvwa.md
├── 05-fingerprinting.md
└── 06-synthese-jour1.md
```

## Organisation

```text
jour-1/
├── support-etudiant/       # Consignes TP à distribuer
├── lab/                    # Docker Compose, scripts, données OSINT simulées
└── livrables-templates/    # Modèles de rendu étudiant
```
