import pygame
import config
prev_button = pygame.Rect(15, 215, 55, 25)
play_button = pygame.Rect(92, 215, 55, 25)
next_button = pygame.Rect(170, 215, 55, 25)
exit_button = pygame.Rect(215,5,20,20)

# kleuren
PANEL = (45, 45, 45)
BUTTON = (60, 60, 60)
BUTTON_HOVER = (90, 90, 90)
GREY = (170, 170, 170)

def format_time(seconds):

    minutes = seconds // 60
    seconds = seconds % 60

    return f"{minutes:02}:{seconds:02}"

def rounded_rect(screen, color, rect, radius=10):

    x, y, w, h = rect

    pygame.draw.rect(
        screen,
        color,
        (x + radius, y, w - 2 * radius, h)
    )

    pygame.draw.rect(
        screen,
        color,
        (x, y + radius, w, h - 2 * radius)
    )

    pygame.draw.circle(
        screen,
        color,
        (x + radius, y + radius),
        radius
    )

    pygame.draw.circle(
        screen,
        color,
        (x + w - radius, y + radius),
        radius
    )

    pygame.draw.circle(
        screen,
        color,
        (x + radius, y + h - radius),
        radius
    )

    pygame.draw.circle(
        screen,
        color,
        (x + w - radius, y + h - radius),
        radius
    )

def rounded_image(surface, radius):

    size = surface.get_size()

    mask = pygame.Surface(
        size,
        pygame.SRCALPHA
    )

    x = 0
    y = 0
    w = size[0]
    h = size[1]

    color = (255, 255, 255)

    pygame.draw.rect(
        mask,
        color,
        (x + radius, y, w - 2 * radius, h)
    )

    pygame.draw.rect(
        mask,
        color,
        (x, y + radius, w, h - 2 * radius)
    )

    pygame.draw.circle(
        mask,
        color,
        (radius, radius),
        radius
    )

    pygame.draw.circle(
        mask,
        color,
        (w - radius, radius),
        radius
    )

    pygame.draw.circle(
        mask,
        color,
        (radius, h - radius),
        radius
    )

    pygame.draw.circle(
        mask,
        color,
        (w - radius, h - radius),
        radius
    )

    result = pygame.Surface(
        size,
        pygame.SRCALPHA
    )

    result.blit(
        surface,
        (0, 0)
    )

    result.blit(
        mask,
        (0, 0),
        special_flags=pygame.BLEND_RGBA_MIN
    )

    return result

def draw_album_cover(screen, cover):

    cover_rect = pygame.Rect(
        60,
        10,
        120,
        120
    )

    # schaduw achter de albumhoes
    pygame.draw.rect(
        screen,
        (0, 0, 0),
        (
            64,
            14,
            120,
            120
        )
    )

    if cover:

        cover_surface = pygame.image.fromstring(
            cover.tobytes(),
            cover.size,
            cover.mode
        )

        cover_surface = rounded_image(
        cover_surface,
        12
        )

        screen.blit(
            cover_surface,
            cover_rect
        )

    else:

        pygame.draw.rect(
            screen,
            (80, 80, 80),
            cover_rect
        )

        font = pygame.font.Font(None, 28)

        text = font.render(
            "♪",
            True,
            config.ACCENT
        )

        rect = text.get_rect(
            center=(120, 75)
        )

        screen.blit(
            text,
            rect
        )


def draw_text_info(screen, metadata):

    title_font = pygame.font.Font(None, 22)
    info_font = pygame.font.Font(None, 18)

    title = metadata.get(
        "title",
        "Onbekende titel"
    )

    artist = metadata.get(
        "artist",
        "Onbekende artiest"
    )

    album = metadata.get(
        "album",
        "Onbekend album"
    )


    # tekst niet buiten het scherm laten lopen
    def shorten(text, length):
        if len(text) > length:
            return text[:length-3] + "..."
        return text


    title = shorten(title, 22)
    artist = shorten(artist, 16)
    album = shorten(album, 14)


    screen.blit(
        title_font.render(
            title,
            True,
            config.TEXT
        ),
        (10, 140)
    )


    screen.blit(
        info_font.render(
            artist,
            True,
            (170,170,170)
        ),
        (10, 157)
    )


    screen.blit(
        info_font.render(
            album,
            True,
            (170,170,170)
        ),
        (10, 174)
    )


def draw_progress(screen, current_time, total_time):

    # achtergrond balk
    pygame.draw.rect(
        screen,
        (60, 60, 60),
        (15, 205, 200, 8)
    )

    # berekening voortgang
    if total_time > 0:
        progress = current_time / total_time
    else:
        progress = 0

    width = int(210 * progress)

    # voortgang
    pygame.draw.rect(
        screen,
        config.ACCENT,
        (15, 205, width, 8)
    )

    font = pygame.font.Font(None, 16)

    def format_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    time_text = (
        format_time(current_time)
        + " / "
        + format_time(total_time)
    )

    time = font.render(
        time_text,
        True,
        config.TEXT
    )

    screen.blit(time, (90, 190))


def draw_buttons(screen, mouse_pos, playing):

    if playing:
       play_symbol = "||"
    else:
       play_symbol = ">"

    buttons = [
    ("<<", prev_button),
    (play_symbol, play_button),
    (">>", next_button),
    ("X", exit_button),
]

    font = pygame.font.Font(None, 25)

    for text, rect in buttons:

        color = BUTTON

        if rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER

        rounded_rect(
            screen,
            color,
            rect,
            8
        )

        label = font.render(
            text,
            True,
            config.TEXT
        )

        label_rect = label.get_rect(
            center=rect.center
        )

        screen.blit(label, label_rect)


def draw_player(screen,mouse_pos,cover=None,metadata=None,current_time=0,total_time=0,current_song=0,total_songs=0,playing=False):

    screen.fill(config.BACKGROUND)

    draw_album_cover(screen, cover)
    draw_text_info(screen, metadata)
    draw_progress(screen,current_time,total_time)
    draw_buttons(screen,mouse_pos,playing)
    draw_track_number(screen,current_song,total_songs)

    # nummer teller
    font = pygame.font.Font(None, 18)

    

def draw_track_number(screen, current_song, total_songs):

    font = pygame.font.Font(None, 16)

    track_text = (
        str(current_song + 1)
        + " / "
        + str(total_songs)
    )

    text = font.render(
        track_text,
        True,
        config.TEXT
    )

    screen.blit(
        text,
        (180, 140)
    )    