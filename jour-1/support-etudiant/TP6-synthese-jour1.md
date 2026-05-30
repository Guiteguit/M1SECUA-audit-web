# TP6 — Synthèse Jour 1

Durée : 45 min

## Contexte

Vous avez terminé la première journée d'audit :

```text
Préparation du lab
Reconnaissance passive
Reconnaissance active contrôlée
Configuration Burp
Mapping DVWA
Fingerprinting technologique
```

Vous devez maintenant produire une note de synthèse claire pour préparer les tests du jour 2.

## Objectif

Transformer vos observations en plan de test.

À la fin du TP, votre synthèse doit permettre à un autre auditeur de comprendre :

- le périmètre ;
- les services observés ;
- les informations exposées ;
- les endpoints importants ;
- les technologies probables ;
- les risques à vérifier ;
- les tests prioritaires pour la suite.

## Travail demandé

### 1. Créer le livrable de synthèse

Depuis `jour-1/lab` :

```bash
cp ../livrables-templates/06-synthese-jour1.md livrables/06-synthese-jour1.md
```

### 2. Consolider les preuves

Relisez vos livrables précédents :

```text
00-validation-lab.md
01-reconnaissance-passive.md
02-reconnaissance-active.md
03-configuration-burp.md
04-mapping-dvwa.md
05-fingerprinting.md
```

Ne recopiez pas tout. Sélectionnez les éléments utiles pour la suite de l'audit.

### 3. Décrire le périmètre

Indiquez clairement :

```text
Domaine : target.local
Application principale : http://dvwa.target.local:8081
Documentation : http://docs.target.local:8082
Hors périmètre : Internet, réseau école, machines des autres étudiants
```

### 4. Prioriser les surfaces de test

Classez les endpoints DVWA selon l'intérêt pour les jours suivants.

Exemple de logique :

```text
Endpoint avec paramètre utilisateur -> priorité haute
Endpoint sans paramètre -> priorité moyenne ou basse
Endpoint lié à upload/session/auth -> priorité haute
```

### 5. Rédiger les hypothèses de risque

Chaque hypothèse doit suivre le format :

```text
Observation :
Risque potentiel :
Preuve actuelle :
Test prévu :
Priorité :
```

Exemple :

```text
Observation : /vulnerabilities/sqli/ expose un paramètre id.
Risque potentiel : injection SQL.
Preuve actuelle : endpoint observé dans Burp, paramètre GET.
Test prévu : tests SQLi contrôlés au jour 2.
Priorité : haute.
```

### 6. Préparer l'archive finale

Depuis `jour-1/lab` :

```bash
zip -r livrables-jour1-NOM-PRENOM.zip livrables/
```

Remplacez `NOM-PRENOM` par votre nom.

Vérifiez le contenu :

```bash
unzip -l livrables-jour1-NOM-PRENOM.zip
```

## Qualité attendue

Une bonne synthèse :

- sépare les faits des hypothèses ;
- cite les preuves techniques ;
- évite les conclusions non démontrées ;
- prépare clairement le jour 2 ;
- reste lisible pour un lecteur non présent pendant les manipulations.

Une mauvaise synthèse :

- colle uniquement des sorties de commandes ;
- annonce des vulnérabilités sans preuve ;
- oublie le périmètre ;
- ne priorise pas les tests ;
- ne propose aucune suite logique.

## Livrable

Fichier à compléter :

```text
jour-1/lab/livrables/06-synthese-jour1.md
```

Archive finale attendue :

```text
livrables-jour1-NOM-PRENOM.zip
```

## Questions

1. Quelle différence faites-vous entre observation, hypothèse et vulnérabilité confirmée ?
2. Pourquoi la synthèse du jour 1 prépare-t-elle directement les tests du jour 2 ?
3. Quels éléments doivent absolument apparaître dans une note d'audit exploitable ?
4. Pourquoi faut-il prioriser les tests plutôt que tout tester sans ordre ?
