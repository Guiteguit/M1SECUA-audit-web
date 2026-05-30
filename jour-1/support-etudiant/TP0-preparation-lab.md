# TP0 — Préparation du lab Kali

Durée : 30 à 45 min

## Contexte

Vous commencez une mission d'audit web dans un environnement de laboratoire local.

Le client fictif expose deux services :

```text
http://dvwa.target.local:8081   Application volontairement vulnérable
http://docs.target.local:8082   Portail documentaire OSINT simulé
```

Le but de ce TP est de préparer votre poste Kali et de vérifier que le lab est fonctionnel avant de commencer la reconnaissance.

## Objectif

À la fin du TP, vous devez être capable de prouver que :

- Docker fonctionne ;
- les conteneurs du lab sont démarrés ;
- les noms locaux `dvwa.target.local` et `docs.target.local` résolvent bien vers votre machine ;
- les deux services HTTP répondent ;
- un dossier de livrables est prêt pour documenter la journée.

## Périmètre autorisé

Les manipulations sont strictement limitées à :

```text
127.0.0.1
*.target.local
ports 8081 et 8082
```

Ne lancez aucun scan ou outil offensif vers Internet, le réseau de l'école ou la machine d'un autre étudiant.

## Travail demandé

### 1. Se placer dans le bon dossier

Depuis la racine du dépôt :

```bash
cd jour-1/lab
pwd
```

Vous devez être dans :

```text
M1SECUA-audit-web/jour-1/lab
```

### 2. Préparer les scripts

```bash
chmod +x setup-kali.sh check-lab.sh
```

Cette commande rend les scripts exécutables sur Linux.

### 3. Installer les outils utiles

```bash
./setup-kali.sh
```

Le script installe ou vérifie notamment :

- Docker : moteur de conteneurisation utilisé pour lancer les applications du lab sans installer manuellement tous leurs composants ;
- `curl` : client HTTP en ligne de commande, utile pour tester rapidement une URL, des headers ou un code de réponse ;
- `whatweb` : outil de fingerprinting web qui aide à identifier des technologies, frameworks, serveurs et CMS ;
- `nmap` : scanner réseau utilisé ici uniquement pour identifier les services exposés sur les ports autorisés du lab ;
- `ffuf` : outil de fuzzing web utilisé pour découvrir des chemins ou fichiers à partir d'une wordlist contrôlée ;
- `nikto` : scanner web orienté mauvaises configurations et fichiers connus, à utiliser avec prudence et uniquement dans le périmètre autorisé ;
- `zip` : outil d'archivage utilisé pour préparer le rendu final des livrables.

Il ajoute aussi les noms locaux du lab dans `/etc/hosts`.

Si le script vous indique de vous déconnecter/reconnecter pour Docker, faites-le avant de continuer.

### 4. Vérifier la résolution locale

```bash
getent hosts dvwa.target.local
getent hosts docs.target.local
```

Résultat attendu :

```text
127.0.0.1 dvwa.target.local
127.0.0.1 docs.target.local
```

Si ces noms ne résolvent pas, le navigateur et les outils ne trouveront pas les cibles du lab.

### 5. Démarrer les services

```bash
docker compose up -d
```

Cette commande lit le fichier `docker-compose.yml` présent dans le dossier `jour-1/lab`.

Dans ce lab, Docker Compose démarre deux conteneurs :

```text
dvwa        Application web volontairement vulnérable, exposée sur http://dvwa.target.local:8081
osint-docs  Serveur Nginx qui publie les documents OSINT simulés sur http://docs.target.local:8082
```

Concrètement :

- Docker télécharge les images nécessaires si elles ne sont pas déjà présentes ;
- Docker crée les conteneurs décrits dans `docker-compose.yml` ;
- le port `8081` de votre machine est redirigé vers le port web du conteneur DVWA ;
- le port `8082` de votre machine est redirigé vers le serveur documentaire ;
- l'option `-d` lance les conteneurs en arrière-plan, pour récupérer le terminal.

Vérifiez les conteneurs :

```bash
docker ps
```

Vous devez voir au minimum :

```text
dvwa
osint-docs
```

### 6. Tester les accès HTTP

```bash
curl -I http://dvwa.target.local:8081
curl -I http://docs.target.local:8082
```

Vous devez obtenir une réponse HTTP, par exemple `200`, `302` ou une réponse serveur exploitable pour l'audit.

Lancez ensuite le script de contrôle :

```bash
./check-lab.sh
```

### 7. Créer le livrable du TP

Depuis `jour-1/lab` :

```bash
mkdir -p livrables
cp ../livrables-templates/00-validation-lab.md livrables/00-validation-lab.md
```

Complétez le fichier avec :

- votre OS ;
- la date ;
- le résultat de `docker ps` ;
- les tests HTTP vers DVWA et le portail documentaire.

## Dépannage rapide

### Docker refuse les commandes sans sudo

Déconnectez-vous puis reconnectez-vous, ou redémarrez la session Kali. Le script ajoute votre utilisateur au groupe `docker`, mais cette modification n'est prise en compte qu'à la nouvelle session.

### Le nom `dvwa.target.local` ne résout pas

Vérifiez :

```bash
grep -n "M1SECUA Jour 1 lab" /etc/hosts
getent hosts dvwa.target.local
```

Relancez `./setup-kali.sh` si nécessaire.

### Un port est déjà utilisé

Vérifiez :

```bash
ss -ltnp | grep -E ":8081|:8082"
```

Arrêtez le service en conflit ou demandez au formateur avant de modifier `docker-compose.yml`.

## Livrable

Fichier à compléter :

```text
jour-1/lab/livrables/00-validation-lab.md
```

## Questions

1. Pourquoi le lab utilise-t-il des noms locaux comme `dvwa.target.local` plutôt que seulement `127.0.0.1` ?
2. Pourquoi faut-il vérifier le périmètre avant de lancer des outils d'audit ?
3. Quelle différence faites-vous entre un conteneur démarré et un service web réellement accessible ?
