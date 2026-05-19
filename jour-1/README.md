# Jour 1 — Méthodologies d'audit et reconnaissance

## Objectifs pédagogiques

À la fin de cette journée, vous devez être capables de :

- comprendre le rôle d'une méthodologie d'audit ;
- différencier reconnaissance passive et active ;
- préparer un lab local légal ;
- configurer Burp Suite ;
- mapper une application web ;
- identifier technologies, paramètres, cookies et surfaces d'attaque ;
- produire une première synthèse d'audit.

## Déroulé recommandé

| Créneau | Contenu |
|---|---|
| 09h00–09h30 | Cadre légal, objectifs, méthodologies OWASP/NIST |
| 09h30–10h15 | Théorie reconnaissance passive/active |
| 10h15–11h00 | TP0 — Préparation du lab |
| 11h00–12h15 | TP1 — Reconnaissance passive locale |
| 13h30–14h15 | TP2 — Reconnaissance active contrôlée |
| 14h15–15h00 | TP3 — Configuration Burp Suite |
| 15h00–16h15 | TP4 — Mapping DVWA |
| 16h15–16h45 | TP5 — Fingerprinting |
| 16h45–17h30 | TP6 — Synthèse et restitution |

## Lab

```bash
cd jour-1/lab
docker compose up -d
./check-lab.sh
```
