import pygame
import config


def draw_splash(screen):

    screen.fill(config.BACKGROUND)

    font_big = pygame.font.Font(None, 32)
    font_small = pygame.font.Font(None, 18)

    title = font_big.render(
        "PiPlayer",
        True,
        config.TEXT
    )

    version = font_small.render(
        "Version 1.0",
        True,
        config.TEXT
    )

    loading = font_small.render(
        "Laaden...",
        True,
        config.ACCENT
    )

    screen.blit(
        title,
        title.get_rect(
            center=(120, 90)
        )
    )

    screen.blit(
        version,
        version.get_rect(
            center=(120, 120)
        )
    )

    screen.blit(
        loading,
        loading.get_rect(
            center=(120, 160)
        )
    )

    pygame.display.update()