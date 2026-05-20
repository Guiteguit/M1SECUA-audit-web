# J4-C01 — Corrélation DAST/SAST

## Objectif
Relier une vulnérabilité observée dynamiquement à un pattern de code vulnérable.

## Consignes
1. Choisir SQLi, XSS, SSRF, XXE ou désérialisation.
2. Décrire la preuve dynamique.
3. Identifier un pattern équivalent dans le code de lab.
4. Expliquer la cause racine.
5. Proposer une règle de détection automatisable.

## Exemples
| Vuln dynamique | Pattern code |
|---|---|
| SQLi | concaténation entrée utilisateur dans SQL |
| SSRF | `requests.get(url)` sur URL utilisateur |
| XXE | parseur XML avec entités externes |
| Désérialisation | `pickle.loads(user_input)` |
| XSS | sortie HTML non encodée |

## Preuve attendue
Vulnérabilité dynamique, pattern de code, cause racine, remédiation.
