# M1SECUA — Sécurité Web Avancée et Audit

Dépôt pédagogique du module **Sécurité Web Avancée et Audit — Master 1**.

Ce dépôt contient les supports étudiants, les laboratoires techniques, les scripts de démarrage et les templates de livrables pour un cours intensif de 5 jours autour de l’audit de sécurité applicative.

---

## Objectif du module

L’objectif du module est de former les étudiants à une démarche complète d’audit applicatif :

```text
Cadrage → Reconnaissance → Exploitation contrôlée → Authentification / Autorisation
→ Automatisation / Code Review → Rapport d’audit → Remédiation
```

Le fil rouge consiste à auditer des applications vulnérables dans un environnement de laboratoire légal et contrôlé.

---

## Programme des 5 jours

| Jour | Thème | Objectifs principaux |
|---|---|---|
| Jour 1 | Méthodologies d’audit et reconnaissance | OWASP WSTG, NIST SP 800-115, OSINT simulé, reconnaissance active contrôlée, Burp Suite, mapping applicatif |
| Jour 2 | Vulnérabilités avancées et exploitation | SQL Injection, XSS, XXE, SSRF, désérialisation non sécurisée |
| Jour 3 | Authentification et autorisation | Brute-force, sessions, CSRF, IDOR, privilege escalation, OAuth 2.0 / OIDC, JWT |
| Jour 4 | Audit automatisé et Code Review | SAST, SonarQube, Bandit, ESLint Security, code review manuelle, DevSecOps CI/CD |
| Jour 5 | Rapport d’audit et remédiation | Executive Summary, findings techniques, CVSS, plan de remédiation, secure coding, restitution orale |

---

## Cadre légal

Les manipulations sont strictement limitées aux environnements de laboratoire fournis dans ce dépôt.

Les étudiants ne doivent jamais utiliser les techniques, outils ou payloads sur :

- des sites publics ;
- des adresses IP externes ;
- le réseau de l’école ;
- la machine d’un autre étudiant ;
- des applications réelles non explicitement autorisées ;
- des API ou services cloud non prévus dans le TP.

Chaque journée précise son propre périmètre autorisé.

Règle simple :

```text
Je teste uniquement ce qui est explicitement autorisé dans le TP.
```

---

## Organisation du dépôt

```text
M1SECUA-audit-web/
├── README.md
├── jour-1/
│   ├── README.md
│   ├── support-etudiant/
│   ├── lab/
│   └── livrables-templates/
├── jour-2/
│   ├── README.md
│   ├── support-etudiant/
│   ├── lab/
│   └── livrables-templates/
├── jour-3/
│   ├── README.md
│   ├── support-etudiant/
│   ├── lab/
│   └── livrables-templates/
├── jour-4/
│   ├── README.md
│   ├── support-etudiant/
│   ├── lab/
│   └── livrables-templates/
└── jour-5/
    ├── README.md
    ├── support-etudiant/
    ├── lab/
    └── livrables-templates/
```

---

## Prérequis étudiants

Chaque étudiant doit disposer de :

- Kali Linux ou une VM Linux compatible ;
- Docker ;
- Docker Compose ;
- Burp Suite Community ou Professional ;
- Firefox ou Chromium ;
- Git ;
- accès au dépôt GitHub.

Les scripts de chaque journée installent les outils nécessaires autant que possible.

---

## Installation initiale

Cloner le dépôt :

```bash
git clone https://github.com/<ORG_OU_USER>/M1SECUA-audit-web.git
cd M1SECUA-audit-web
```

Remplacer `<ORG_OU_USER>` par l’organisation ou le compte GitHub utilisé par l’école ou le formateur.

---

## Démarrage rapide par journée

### Jour 1 — Méthodologies et reconnaissance

```bash
cd jour-1/lab
chmod +x setup-kali.sh check-lab.sh
./setup-kali.sh
docker compose up -d
./check-lab.sh
```

Supports :

```text
jour-1/support-etudiant/
```

---

### Jour 2 — Vulnérabilités avancées

```bash
cd jour-2/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d --build
./check-lab.sh
```

Supports :

```text
jour-2/support-etudiant/
```

---

### Jour 3 — Authentification et autorisation

```bash
cd jour-3/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d --build
./check-lab.sh
```

Supports :

```text
jour-3/support-etudiant/
```

---

### Jour 4 — Audit automatisé et Code Review

```bash
cd jour-4/lab
chmod +x setup-kali.sh check-lab.sh reset-lab.sh
./setup-kali.sh
docker compose up -d --build
./check-lab.sh
```

Supports :

```text
jour-4/support-etudiant/
```

---

### Jour 5 — Rapport d’audit et remédiation

```bash
cd jour-5/lab
chmod +x scripts/*.sh
./scripts/check-tools.sh
./scripts/init-report.sh
```

Supports :

```text
jour-5/support-etudiant/
```

---

## Rendus attendus

Chaque journée produit une archive de livrables.

| Jour | Archive attendue |
|---|---|
| Jour 1 | `livrables-jour1-NOM-PRENOM.zip` |
| Jour 2 | `livrables-jour2-NOM-PRENOM.zip` |
| Jour 3 | `livrables-jour3-NOM-PRENOM.zip` |
| Jour 4 | `livrables-jour4-NOM-PRENOM.zip` |
| Jour 5 | `livrables-jour5-NOM-PRENOM.zip` |

Les livrables sont généralement produits dans :

```text
jour-X/lab/livrables/
```

---

## Méthode de travail recommandée

Pour chaque TP :

1. lire le support étudiant ;
2. respecter le périmètre autorisé ;
3. exécuter les commandes demandées ;
4. observer les résultats ;
5. documenter les preuves ;
6. expliquer l’impact ;
7. proposer une remédiation ;
8. compléter le livrable associé.

Le but n’est pas uniquement d’obtenir un résultat technique, mais de comprendre et documenter la démarche d’audit.

---

## Bonnes pratiques de sécurité

Ne jamais pousser dans GitHub :

- des vrais mots de passe ;
- des tokens ;
- des clés privées ;
- des captures contenant des données personnelles ;
- des rapports contenant des informations réelles non anonymisées.

Les secrets utilisés dans les TP sont fictifs et uniquement destinés au laboratoire pédagogique.

---

## Philosophie du module

Un bon auditeur ne se limite pas à exécuter des outils.

Il doit savoir :

```text
comprendre le périmètre,
identifier les surfaces d’attaque,
tester de manière contrôlée,
documenter les preuves,
évaluer le risque,
prioriser les corrections,
communiquer clairement avec les parties prenantes.
```

L’exploitation technique est importante, mais la capacité à expliquer, prioriser et remédier l’est tout autant.

---

## Avertissement

Ce dépôt est fourni uniquement à des fins pédagogiques.

Les techniques présentées doivent être utilisées exclusivement dans les environnements de laboratoire autorisés.
Toute utilisation sur un système tiers sans autorisation explicite est interdite.
