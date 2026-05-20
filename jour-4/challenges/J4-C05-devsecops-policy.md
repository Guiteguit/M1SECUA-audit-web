# J4-C05 — Politique DevSecOps minimale

## Objectif
Définir une politique de sécurité CI/CD réaliste.

## Questions
1. Quels scans lancer en merge request ?
2. Quels contrôles sont bloquants ?
3. Quels contrôles sont informatifs ?
4. Comment gérer les faux positifs ?
5. Qui valide une exception ?
6. Où stocker les rapports ?
7. Comment vérifier une correction ?

## Contrôles possibles
| Contrôle | Outil |
|---|---|
| SAST Python | Bandit |
| SAST JS | ESLint Security |
| Dépendances | pip-audit / npm audit |
| Secrets | gitleaks |
| Containers | trivy |
| DAST local | ZAP/Burp/scripts |

## Preuve attendue
Tableau des contrôles, seuils bloquants, stratégie faux positifs, processus d’exception.
