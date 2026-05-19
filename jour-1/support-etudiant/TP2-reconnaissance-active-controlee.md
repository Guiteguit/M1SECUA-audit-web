# TP2 — Reconnaissance active contrôlée

## Objectif
Envoyer des requêtes uniquement vers le lab local.

## Commandes
```bash
nmap -sV -p 8081,8082 127.0.0.1
curl -I http://dvwa.target.local:8081
curl -I http://docs.target.local:8082
whatweb http://dvwa.target.local:8081
whatweb http://docs.target.local:8082
ffuf -u http://dvwa.target.local:8081/FUZZ -w wordlists/wordlist-lab.txt -mc all
```

## Livrable
```bash
cp ../livrables-templates/02-reconnaissance-active.md livrables/02-reconnaissance-active.md
```
