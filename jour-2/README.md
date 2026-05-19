# Jour 2 — Vulnérabilités avancées et exploitation

## Objectifs pédagogiques

À la fin du Jour 2, vous devez être capables de :

- exploiter une SQL Injection de manière contrôlée ;
- différencier Union-based, Boolean Blind et Time-based SQL Injection ;
- identifier et tester une XSS reflected, stored et DOM ;
- comprendre le principe d’une XXE ;
- comprendre et tester une SSRF en environnement local ;
- comprendre le risque de désérialisation non sécurisée ;
- qualifier les vulnérabilités avec une première approche CVSS ;
- documenter proprement les preuves techniques.

## Cadre légal

Les manipulations sont strictement limitées au lab local.

Cibles autorisées :

- `http://dvwa.target.local:8081`
- `http://juice.target.local:3000`
- `http://webgoat.target.local:8080/WebGoat`
- `http://vulnapi.target.local:5000`
- `http://internal.target.local:8088`
- `127.0.0.1`

Interdictions : sites Internet réels, réseau de l’école, machine d’un autre étudiant, données réelles.

## Démarrage rapide

```bash
cd jour-2/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d --build
./check-lab.sh
```

## Déroulé des TP

1. `TP0-preparation-lab-jour2.md`
2. `TP1-sql-injection-dvwa.md`
3. `TP2-xss-dvwa-juice-shop.md`
4. `TP3-xxe-webgoat-vulnapi.md`
5. `TP4-ssrf-vulnapi.md`
6. `TP5-deserialisation-vulnapi.md`
7. `TP6-cvss-synthese.md`

## Livrables attendus

```text
livrables/
├── 00-validation-lab-jour2.md
├── 01-sqli.md
├── 02-xss.md
├── 03-xxe.md
├── 04-ssrf.md
├── 05-deserialisation.md
└── 06-cvss-synthese.md
```
