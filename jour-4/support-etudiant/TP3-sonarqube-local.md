# TP3 — SonarQube local

## Objectif

Démarrer SonarQube et comprendre son rôle dans un audit automatisé.

## Étape 1 — Ouvrir SonarQube

```text
http://localhost:9000
```

Identifiants par défaut :

```text
admin / admin
```

SonarQube peut demander de changer le mot de passe au premier login.

## Étape 2 — Créer un projet local

Dans l’interface :

1. Create Project
2. Local project
3. Project key : `m1secua-jour4-python`
4. Generate token
5. Choisir analyse locale

## Étape 3 — Installer sonar-scanner

Si non présent, utiliser le scanner Docker ou suivre les instructions affichées par SonarQube.

Option simple : documenter les étapes et résultats observés dans l’UI.

## Étape 4 — Analyser les résultats

Observer :

- bugs ;
- vulnerabilities ;
- code smells ;
- security hotspots ;
- duplication ;
- dette technique.

## Livrable

```bash
cp ../livrables-templates/03-sonarqube.md livrables/03-sonarqube.md
```

## Point d’attention

L’objectif principal est de comprendre le dashboard et la logique SonarQube.
Le TP reste valide si l’analyse complète nécessite une adaptation selon la VM.
