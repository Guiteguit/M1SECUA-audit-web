#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter

findings_file = Path("findings/findings-jours1-4-sample.json")
findings = json.loads(findings_file.read_text(encoding="utf-8"))

counter = Counter(f["severity"] for f in findings)

print("# Synthèse automatique des findings")
print()
print("| Sévérité | Nombre |")
print("|---|---:|")
for sev in ["Critical", "High", "Medium", "Low", "Informational"]:
    print(f"| {sev} | {counter.get(sev, 0)} |")

print()
print("## Findings")
print()
print("| ID | Sévérité | Titre | Endpoint / Fichier |")
print("|---|---|---|---|")
for f in findings:
    print(f"| {f['id']} | {f['severity']} | {f['title']} | {f['endpoint']} |")
