# Jour 3 — Authentification et Autorisation

## Objectifs pédagogiques

À la fin du Jour 3, vous devez être capables de :

- auditer un mécanisme d’authentification ;
- identifier l’absence de rate limiting ;
- analyser des cookies de session ;
- comprendre session hijacking, fixation et flags de cookies ;
- tester une faille CSRF dans un lab ;
- exploiter une IDOR locale ;
- identifier une élévation de privilèges par contrôle d’accès insuffisant ;
- analyser une implémentation OAuth 2.0 / OIDC faible ;
- comprendre et tester des failles JWT dans un environnement contrôlé.

## Cadre légal

Les manipulations sont strictement limitées au lab local.

Cibles autorisées :

- `http://dvwa.target.local:8081`
- `http://webgoat.target.local:8080/WebGoat`
- `http://juice.target.local:3000`
- `http://authapi.target.local:5001`
- `127.0.0.1`

Interdictions :

- tester des portails réels ;
- brute-forcer des services externes ;
- utiliser ces techniques hors lab ;
- scanner le réseau de l’école ;
- attaquer la machine d’un autre étudiant.

## Démarrage rapide

```bash
cd jour-3/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d --build
./check-lab.sh
```

## Déroulé des TP

1. `TP0-preparation-lab-jour3.md`
2. `TP1-audit-authentification.md`
3. `TP2-sessions-csrf.md`
4. `TP3-idor-privilege-escalation.md`
5. `TP4-jwt-vulnerabilites.md`
6. `TP5-oauth-oidc-audit.md`
7. `TP6-synthese-jour3.md`

## Livrables attendus

```text
livrables/
├── 00-validation-lab-jour3.md
├── 01-authentification.md
├── 02-sessions-csrf.md
├── 03-idor-privilege-escalation.md
├── 04-jwt.md
├── 05-oauth-oidc.md
└── 06-synthese-jour3.md
```
