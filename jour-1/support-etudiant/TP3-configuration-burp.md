# TP3 — Configuration de Burp Suite

## Objectif
Configurer Firefox avec Burp en proxy `127.0.0.1:8080`.

## Étapes
1. Lancer Burp : `burpsuite`.
2. Vérifier le listener dans `Proxy > Proxy settings`.
3. Configurer Firefox : proxy HTTP/HTTPS `127.0.0.1:8080`.
4. Ouvrir `http://dvwa.target.local:8081`.
5. Vérifier `Proxy > HTTP history`.
6. Tester `Intercept ON/OFF`.
7. Envoyer une requête dans `Repeater`.

## Livrable
```bash
cp ../livrables-templates/03-configuration-burp.md livrables/03-configuration-burp.md
```
