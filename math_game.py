import random
import pygame


def generate_problem():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    op = random.choice(['+', '-', '*'])
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = a * b
    return f"{a} {op} {b} =", result


def run(surface):
    """Run a simple math quiz minigame.

    The function draws on ``surface`` until the user enters the correct
    answer to the generated math problem and then returns ``True``. If the
    window is closed ``False`` is returned.
    """
    problem, answer = generate_problem()
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
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    pass
                else:
                    if event.unicode.isdigit() or (event.unicode == '-' and typed == ''):
                        typed += event.unicode

        surface.fill((0, 0, 0))
        prob_surf = font.render(problem, True, (255, 255, 255))
        typed_surf = font.render(typed, True, (0, 255, 0))
        surface.blit(prob_surf, (surface.get_width() // 2 - prob_surf.get_width() // 2,
                                 surface.get_height() // 3))
        surface.blit(typed_surf, (surface.get_width() // 2 - typed_surf.get_width() // 2,
                                  surface.get_height() // 2))
        pygame.display.flip()

        if typed == str(answer):
            return True
        clock.tick(60)
