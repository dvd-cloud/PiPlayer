from mutagen.mp3 import MP3
from mutagen.id3 import ID3


def get_metadata(filename):

    data = {
        "title": "Onbekend",
        "artist": "Onbekend",
        "album": "Onbekend",
        "cover": None
    }

    try:
        audio = MP3(filename, ID3=ID3)

        if audio.tags:

            tags = audio.tags

            if tags.get("TIT2"):
                data["title"] = str(tags["TIT2"])

            if tags.get("TPE1"):
                data["artist"] = str(tags["TPE1"])

            if tags.get("TALB"):
                data["album"] = str(tags["TALB"])

            for tag in tags.values():

                if tag.FrameID == "APIC":
                    data["cover"] = tag.data
                    break

    except Exception as e:
        print("Metadata fout:", e)

    return data


def get_length(filename):

    audio = MP3(filename)

    return int(audio.info.length)