# TP3 — Configuration de Burp Suite

Durée : 45 min

## Contexte

Burp Suite est un proxy d'interception utilisé pour observer, rejouer et modifier des requêtes HTTP dans un audit web.

Dans ce TP, vous ne cherchez pas encore à exploiter une vulnérabilité. Vous préparez l'outillage qui servira à cartographier DVWA et à comprendre les échanges client/serveur.

## Objectif

Configurer Firefox pour faire passer le trafic HTTP du lab dans Burp.

À la fin du TP, vous devez prouver que :

- Burp écoute sur `127.0.0.1:8080` ;
- Firefox utilise Burp comme proxy ;
- les requêtes vers DVWA apparaissent dans `HTTP history` ;
- vous savez activer/désactiver l'interception ;
- vous savez envoyer une requête dans `Repeater`.

## Périmètre autorisé

Utilisez Burp uniquement sur :

```text
http://dvwa.target.local:8081
http://docs.target.local:8082
```

Ne proxifiez pas votre navigation personnelle, vos comptes réels ou des sites externes pendant le TP.

## Travail demandé

### 1. Lancer Burp Suite

```bash
burpsuite
```

Choisissez un projet temporaire si Burp le demande.

### 2. Vérifier le proxy listener

Dans Burp :

```text
Proxy > Proxy settings
```

Vérifiez qu'un listener existe sur :

```text
127.0.0.1:8080
```

Si un autre outil utilise déjà le port `8080`, demandez au formateur avant de modifier la configuration.

### 3. Configurer Firefox

Dans Firefox :

```text
Settings > Network Settings > Manual proxy configuration
```

Configurez :

```text
HTTP Proxy : 127.0.0.1
Port       : 8080
HTTPS Proxy: 127.0.0.1
Port       : 8080
```

Pour ce jour 1, les applications du lab sont en HTTP. L'installation du certificat Burp n'est donc pas indispensable ici, mais elle sera utile dans un audit HTTPS réel.

### 4. Vérifier le trafic dans Burp

Dans Firefox, ouvrez :

```text
http://dvwa.target.local:8081
```

Dans Burp :

```text
Proxy > HTTP history
```

Vous devez voir les requêtes HTTP générées par le navigateur.

### 5. Comprendre Intercept ON/OFF

Dans Burp :

```text
Proxy > Intercept
```

Testez :

- `Intercept is on` : la requête est bloquée dans Burp avant d'être envoyée ;
- `Intercept is off` : le trafic passe et reste visible dans l'historique.

Bon réflexe : gardez l'interception désactivée pendant la navigation normale, puis activez-la uniquement lorsque vous voulez observer ou modifier une requête précise.

### 6. Envoyer une requête dans Repeater

Dans `HTTP history` :

1. sélectionnez une requête vers DVWA ;
2. clic droit ;
3. `Send to Repeater` ;
4. ouvrez l'onglet `Repeater` ;
5. cliquez sur `Send`.

Observez :

- la méthode HTTP ;
- le chemin ;
- les headers ;
- les cookies ;
- le code de réponse ;
- le contenu de réponse.

### 7. Prendre une première note de méthode

Dans votre livrable, expliquez en une phrase le rôle de chaque onglet :

```text
Proxy
HTTP history
Intercept
Repeater
```

## Dépannage rapide

### Firefox n'affiche plus aucune page

Vérifiez que Burp est ouvert et que le listener `127.0.0.1:8080` est actif.

### Burp ne voit aucune requête

Vérifiez :

- proxy Firefox ;
- URL du lab ;
- Burp ouvert ;
- pas de mode proxy système contradictoire.

### Les requêtes restent bloquées

Vérifiez si `Intercept is on`. Cliquez sur `Forward` ou désactivez l'interception.

## Livrable

Créez le fichier :

```bash
cp ../livrables-templates/03-configuration-burp.md livrables/03-configuration-burp.md
```

Complétez avec :

- une preuve que Burp intercepte ou journalise le trafic ;
- une requête envoyée dans Repeater ;
- vos observations sur les headers et cookies vus dans Burp.

## Questions

1. Quelle différence faites-vous entre `HTTP history` et `Repeater` ?
2. Pourquoi faut-il éviter de laisser `Intercept ON` en permanence ?
3. Pourquoi ne faut-il pas proxifier des comptes personnels ou des sites externes pendant le TP ?
