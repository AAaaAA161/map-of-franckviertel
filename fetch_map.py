"""
Lädt die vollständigen MapHub-Kartendaten inkl. Bilder via API
und speichert sie als franckviertel-full.json

Ausführen: python3 fetch_map.py
Benötigt: pip install requests
"""

import json
import requests

API_KEY = "ElExggDfOmcYBG0i"
MAP_ID  = 408440
HEADERS = {"Authorization": "Token " + API_KEY}

print(f"Lade Map-Daten für id={MAP_ID} ...")
r = requests.post(
    "https://maphub.net/api/1/map/get",
    json={"map_id": MAP_ID},
    headers=HEADERS
)
print(f"  HTTP {r.status_code}")
r.raise_for_status()
data = r.json()

geojson  = data.get("geojson", {})
features = geojson.get("features", [])
print(f"  Features: {len(features)}")

with open("franckviertel-full.json", "w", encoding="utf-8") as fp:
    json.dump(data, fp, ensure_ascii=False, indent=2)

print("Gespeichert: franckviertel-full.json")
