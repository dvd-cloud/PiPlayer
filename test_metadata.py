from metadata import get_metadata


bestand = "/home/vmware/Music/test.mp3"


info = get_metadata(bestand)


print("Titel :", info["title"])
print("Artiest :", info["artist"])
print("Album :", info["album"])

if info["cover"]:
    print("Albumhoes gevonden")
else:
    print("Geen albumhoes")