# TP1 — SQL Injection avec DVWA

## Objectif
Comprendre et documenter une SQL Injection.

Dans DVWA : `Vulnerabilities > SQL Injection`.

Tester :
```text
1
'
1' OR '1'='1
1' OR '1'='2
1' ORDER BY 1#
1' ORDER BY 2#
1' ORDER BY 3#
1' UNION SELECT 1,2#
```

Envoyer la requête dans Burp Repeater et documenter : point d’entrée, paramètre, payload, réponse, impact, remédiation.

## Remédiation attendue
Requêtes préparées, validation d’entrée, moindre privilège SQL, messages d’erreur génériques.

## Livrable
```bash
cp ../livrables-templates/01-sqli.md livrables/01-sqli.md
```
