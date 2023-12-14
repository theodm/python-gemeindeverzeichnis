# Ein kleines Tool, um das Gemeindeverzeichnis von der Webseite des
# statistischen Bundesamts herunterzuladen und für die weiteren Schritte
# nutzbar zu machen. (Extrahieren, ...)
import os
import urllib.request
import zipfile

TEMP_DIR = "temp"
DATA_DIR = "../data"
DOWNLOAD_URL = "https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GV100ADQ/GV100AD3011.zip?__blob=publicationFile"

# Altes temporäres Verzeichnis löschen, falls
# aus irgendeinem Grund noch vorhanden.
if os.path.exists(TEMP_DIR):
    os.rmdir(TEMP_DIR)

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# Daten herunterladen
urllib.request.urlretrieve(DOWNLOAD_URL, "temp/GV100AD3011.zip")

# Extrahieren
with zipfile.ZipFile("temp/GV100AD3011.zip", "r") as zip_ref:
    zip_ref.extractall("temp")

# Wir wollen nur die GV100AD_??????.txt behalten. Alle anderen Dateien erhalten
# noch Informationen über den Aufbau der Datei und Bemerkungen.
for file in os.listdir("temp"):
    if not file.startswith("GV100AD") or not file.endswith(".txt"):
        os.remove(os.path.join("temp", file))

# Und in unser Datenverzeichnis schieben.
for file in os.listdir("temp"):
    os.rename(os.path.join("temp", file), os.path.join("../data", file))

# Temporäres Verzeichnis löschen
os.rmdir("temp")


