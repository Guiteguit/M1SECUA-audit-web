# TP2 — XSS avec DVWA et Juice Shop

## Objectif
Comprendre XSS reflected, stored et DOM.

## Reflected XSS
Dans DVWA : `Vulnerabilities > XSS Reflected`.

Tester :
```html
test
<img src=x onerror=alert(1)>
```

## Stored XSS
Dans DVWA : `Vulnerabilities > XSS Stored`. Vérifier la persistance après rechargement.

## DOM
Ouvrir `http://juice.target.local:3000` et utiliser DevTools : Elements, Console, Sources, Network.

## Livrable
```bash
cp ../livrables-templates/02-xss.md livrables/02-xss.md
```
