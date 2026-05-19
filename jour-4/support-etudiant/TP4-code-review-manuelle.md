# TP4 — Code review sécurité manuelle

## Objectif

Lire le code et identifier les vulnérabilités que les outils peuvent manquer ou mal qualifier.

## Fichiers à analyser

```text
sample-python-app/src/app.py
sample-python-app/src/config.py
sample-js-app/src/server.js
```

## Checklist

Pour chaque fonction sensible, vérifier :

- validation des entrées ;
- authentification ;
- autorisation ;
- injection SQL/commande ;
- désérialisation ;
- secrets hardcodés ;
- crypto faible ;
- erreurs trop bavardes ;
- logs ;
- rate limiting ;
- encodage de sortie.

## Commandes utiles

```bash
grep -R "password\|secret\|API_KEY" sample-python-app sample-js-app
grep -R "eval\|pickle\|yaml.load\|shell=True\|md5" sample-python-app sample-js-app
grep -R "execute\|query\|redirect\|send" sample-python-app sample-js-app
```

## Livrable

```bash
cp ../livrables-templates/04-code-review-manuelle.md livrables/04-code-review-manuelle.md
```
