# J2-C01 — SQL Injection contrôlée avec DVWA

## Objectif
Prouver qu’un paramètre est vulnérable à une SQL Injection.

## Cible autorisée
`http://dvwa.target.local:8081/vulnerabilities/sqli/`

## Consignes
1. Se connecter à DVWA.
2. Régler `DVWA Security` sur `Low`.
3. Envoyer une requête normale avec `id=1`.
4. Envoyer la requête dans Burp Repeater.
5. Tester progressivement : erreur, condition vraie, condition fausse, ORDER BY, UNION SELECT.

## Payloads autorisés
```text
'
1' OR '1'='1
1' OR '1'='2
1' ORDER BY 1-- -
1' ORDER BY 2-- -
1' ORDER BY 3-- -
1' UNION SELECT 1,2-- -
```

## Preuve attendue
Endpoint, paramètre, payload, différence de réponse, nombre de colonnes probable, impact, remédiation.
