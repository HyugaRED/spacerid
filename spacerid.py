#!/usr/bin/env python3

print("\n=== SP ID – OSINT Identity Scanner v1 ===\n")

import argparse
import requests
import json
import os
import sys

# Fonction de chargement sécurisé du fichier JSON
def load_platforms():
    path = "platforms.json"
    if not os.path.exists(path):
        print("[!!] Erreur : platforms.json est introuvable.")
        sys.exit(1)

    try:
        with open(path, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict) or not data:
                print("[!!] Erreur : platforms.json est vide ou mal formé.")
                sys.exit(1)
            return data
    except json.JSONDecodeError:
        print("[!!] Erreur : platforms.json contient une erreur de syntaxe JSON.")
        sys.exit(1)

# Charger les plateformes
sites = load_platforms()

# Analyse des arguments
parser = argparse.ArgumentParser(description="SpecterID - Basic OSINT Pseudo Scanner")
parser.add_argument("-u", "--username", help="Pseudo à analyser", required=True)
args = parser.parse_args()
username = args.username

# Scan
print(f"\n[+] Lancement du scan OSINT pour : {username}\n")

# Créer un dossier de sortie si inexistant
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Préparer le fichier de sortie
output_file = os.path.join(output_dir, f"{username}_results.txt")
found_accounts = []  # Liste des comptes trouvés

for name, url in sites.items():
    if not url or '{}' not in url:
        continue  # Ignore les entrées vides ou mal formées
    full_url = url.format(username)
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            print(f"[FOUND] {name} : {full_url}")
            found_accounts.append(f"{name}: {full_url}")
        else:
            print(f"[--] {name} : Non trouvé")
    except requests.RequestException:
        print(f"[!!] {name} : Erreur pendant la requête")

# Sauvegarde des résultats trouvés
if found_accounts:
    with open(output_file, "w") as f:
        f.write(f"Résultats OSINT pour: {username}\n\n")
        for line in found_accounts:
            f.write(line + "\n")
    print(f"\n[+] Résultats enregistrés dans : {output_file}")
else:
    print("\n[+] Aucun compte trouvé. Aucun fichier généré.")


print("\n[+] Scan terminé.")
