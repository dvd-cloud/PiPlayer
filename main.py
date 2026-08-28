import pygame
import sys
import gui
import config
from player import MusicPlayer
from music import get_music
from metadata import get_metadata, get_length
from cover import load_cover
import splash

def load_song(index):

    global current_song
    global metadata
    global cover
    global song_length

    current_song = index

    player.load(
        songs[current_song]
    )

    metadata = get_metadata(
        songs[current_song]
    )

    cover = load_cover(
        metadata["cover"]
    )

    song_length = get_length(
        songs[current_song]
    )

    player.play()

    print(
        "Speelt:",
        metadata["title"]
    )

pygame.init()

songs = get_music()

player = MusicPlayer()

current_song = 0

if songs:
    load_song(0)
    print("Geladen:", songs[current_song])

screen = pygame.display.set_mode(
    (config.SCREEN_WIDTH, config.SCREEN_HEIGHT),
    pygame.FULLSCREEN
)

gui_surface = pygame.Surface(
    (
        config.SCREEN_WIDTH,
        config.SCREEN_HEIGHT
    )
)

splash.draw_splash(screen)

pygame.time.delay(2000)

metadata = get_metadata(
    songs[current_song]
)

cover = load_cover(
    metadata["cover"]
)

song_length = get_length(
    songs[current_song]
)


pygame.display.set_caption("PiPlayer")

clock = pygame.time.Clock()

running = True

while running:

    print("GUI loop actief")

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:   

        

                if gui.exit_button.collidepoint(mouse_pos):

                    running = False

                if gui.prev_button.collidepoint(mouse_pos):

                    prev_song = current_song - 1

                    if prev_song < 0:
                        prev_song = len(songs) - 1

                    load_song(prev_song)

                elif gui.play_button.collidepoint(mouse_pos):
                    player.toggle()

                elif gui.next_button.collidepoint(mouse_pos):

                    next_song = current_song + 1

                    if next_song >= len(songs):
                        next_song = 0

                    load_song(next_song)

    
    # VLC meldt het einde van een nummer via zijn eigen state.
    # We controleren dit op de bestaande 1 FPS GUI-loop.
    if player.is_ended():

        next_song = current_song + 1

        if next_song >= len(songs):
            next_song = 0

        load_song(next_song)

    gui.draw_player(screen,mouse_pos,cover,metadata,player.get_position(),song_length,current_song,len(songs),player.playing)

    pygame.display.update()

    clock.tick(1)

player.stop()
player.release()

pygame.quit()

pygame.quit()
sys.exit()

