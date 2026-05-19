# Correction professeur — Jour 1

## Attendus principaux
- Lab : conteneurs `dvwa` et `osint-docs` actifs.
- OSINT : sous-domaines admin, api, staging, jenkins, grafana, dev, docs, dvwa.
- Documents exposés : `admin/password`, chemins DVWA, emails internes.
- Mapping : endpoints DVWA principaux et cookies `PHPSESSID`, `security`.
- Fingerprinting : DVWA = Apache/PHP, docs = nginx.

## Endpoints DVWA attendus
`/login.php`, `/security.php`, `/vulnerabilities/brute/`, `/vulnerabilities/exec/`, `/vulnerabilities/csrf/`, `/vulnerabilities/fi/`, `/vulnerabilities/upload/`, `/vulnerabilities/sqli/`, `/vulnerabilities/sqli_blind/`, `/vulnerabilities/xss_d/`, `/vulnerabilities/xss_r/`, `/vulnerabilities/xss_s/`.

## Paramètres attendus
`username`, `password`, `Login`, `security`, `id`, `Submit`, `name`, `ip`, `page`, `txtName`, `mtxMessage`.
