# TP2 — Analyse JavaScript avec ESLint Security

## Objectif

Analyser une application JavaScript avec ESLint et le plugin sécurité.

## Étape 1 — Installer les dépendances

```bash
cd jour-4/lab/sample-js-app
npm install
```

## Étape 2 — Lancer ESLint

```bash
npm run lint
```

## Étape 3 — Observer le code

Lire :

```bash
cat src/server.js
```

Identifier manuellement :

- `eval()` sur entrée utilisateur ;
- secret hardcodé ;
- open redirect ;
- HTML non encodé ;
- usage de MD5.

## Étape 4 — Générer une sortie exploitable

```bash
npm run lint -- --format json > ../livrables/eslint-report.json || true
```

## Livrable

```bash
cd ..
cp ../livrables-templates/02-eslint-security.md livrables/02-eslint-security.md
```
