# TP1 — Analyse statique Python avec Bandit

## Objectif

Analyser un projet Python volontairement vulnérable avec Bandit.

## Étape 1 — Activer le venv sécurité

```bash
cd jour-4/lab
source .venv-security/bin/activate
```

## Étape 2 — Lancer Bandit

```bash
bandit -r sample-python-app/src
```

## Étape 3 — Générer un rapport JSON

```bash
bandit -r sample-python-app/src -f json -o livrables/bandit-report.json
```

## Étape 4 — Lire les résultats

Identifier au minimum :

- secret hardcodé ;
- usage de `subprocess` avec `shell=True` ;
- usage de `pickle.loads` ;
- usage de `yaml.load` ;
- usage de MD5 ;
- SQL construite par concaténation.

## Étape 5 — Documenter

Pour chaque finding important :

- fichier ;
- ligne ;
- sévérité ;
- confiance ;
- risque ;
- remédiation.

## Livrable

```bash
cp ../livrables-templates/01-bandit-python.md livrables/01-bandit-python.md
```
