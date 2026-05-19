# TP5 — DevSecOps et pipeline CI/CD

## Objectif

Comprendre comment intégrer les contrôles sécurité dans un pipeline.

## Étape 1 — Lire les exemples fournis

```bash
cat pipelines/github-actions-security.yml
cat pipelines/gitlab-ci-security.yml
```

## Étape 2 — Identifier les étapes de sécurité

Dans les fichiers pipeline, identifier :

- SAST Python avec Bandit ;
- audit dépendances Python avec pip-audit ;
- SAST JS avec ESLint ;
- audit dépendances JS avec npm audit ;
- artifacts de rapport.

## Étape 3 — Adapter pour GitHub

Créer dans un repo de test :

```text
.github/workflows/security.yml
```

Copier le contenu :

```text
pipelines/github-actions-security.yml
```

## Étape 4 — Adapter pour GitLab

Créer :

```text
.gitlab-ci.yml
```

Copier le contenu :

```text
pipelines/gitlab-ci-security.yml
```

## À documenter

- quelles étapes doivent être bloquantes ?
- quels résultats doivent être seulement informatifs ?
- comment gérer les faux positifs ?
- qui valide les exceptions ?
- où stocker les rapports ?

## Livrable

```bash
cp ../livrables-templates/05-devsecops-pipeline.md livrables/05-devsecops-pipeline.md
```
