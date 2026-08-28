import os


MUSIC_FOLDER = "/home/daan/Music"


def get_music():

    songs = []

    for file in os.listdir(MUSIC_FOLDER):

        if file.lower().endswith(".mp3"):
            songs.append(
                os.path.join(
                    MUSIC_FOLDER,
                    file
                )
            )
            

    songs.sort()

    return songs
if __name__ == "__main__":
    songs = get_music()
    print(songs)    