import pygame
import sys

TARGET_SENTENCE = "Type this sentence to defeat the slime!"


def run(surface):
    """Run a simple speed typing minigame.

    The given ``surface`` will be used for drawing the game. The function
    blocks until the user successfully types ``TARGET_SENTENCE`` and returns
    ``True``. If the window is closed, ``False`` is returned.
    """
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    typed = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                elif event.key == pygame.K_RETURN:
                    # ignore return key
                    pass
                else:
                    typed += event.unicode

        surface.fill((0, 0, 0))
        target_surf = font.render(TARGET_SENTENCE, True, (255, 255, 255))
        typed_surf = font.render(typed, True, (0, 255, 0))
        surface.blit(
            target_surf,
            (surface.get_width() // 2 - target_surf.get_width() // 2, surface.get_height() // 3),
        )
        surface.blit(
            typed_surf,
            (surface.get_width() // 2 - typed_surf.get_width() // 2, surface.get_height() // 2),
        )
        pygame.display.flip()

        if typed == TARGET_SENTENCE:
            return True
        clock.tick(60)
