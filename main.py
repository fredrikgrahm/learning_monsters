import pygame
import sys
from player import Player
from map import GameMap 

# Init
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Learning Monsters")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Game objects
game_map = GameMap()
player = Player((200, 64))  # Placed on a walkable tile

# Encounter object placed near the bottom-right corner on a walkable tile
ENCOUNTER_POS = (18 * game_map.tile_size, 14 * game_map.tile_size)
ENCOUNTER2_POS = (10 * game_map.tile_size, 8 * game_map.tile_size)
encounter2_rect = pygame.Rect(ENCOUNTER2_POS, (game_map.tile_size, game_map.tile_size))
encounter_rect = pygame.Rect(ENCOUNTER_POS, (game_map.tile_size, game_map.tile_size))

# Game loop
while True:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.update(keys, game_map)

    # Check for encounter collision (either encounter)
    encounter_triggered = (
        player.rect.colliderect(encounter_rect) or
        player.rect.colliderect(encounter2_rect)
    )

    # Draw map and player
    game_map.draw(screen)
    # Draw the encounter objects as red squares
    pygame.draw.rect(screen, (200, 0, 0), encounter_rect)
    pygame.draw.rect(screen, (200, 0, 0), encounter2_rect)
    player.draw(screen)

    if encounter_triggered:
        text = font.render("Combat", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(60)
