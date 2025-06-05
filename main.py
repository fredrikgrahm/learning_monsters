import pygame
import sys
from player import Player
from map import GameMap
from encounter import EncounterManager

# Init
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Learning Monsters")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Game objects
game_map = GameMap()
player = Player((200, 64))  # Placed on a walkable tile

# Encounter manager handles encounter zones and collisions
encounters = EncounterManager(game_map)

# Game loop
while True:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.update(keys, game_map)

    # Check for encounter collision
    encounter_triggered = encounters.check_trigger(player.rect)

    # Draw map, encounters and player
    game_map.draw(screen)
    encounters.draw(screen)
    player.draw(screen)

    if encounter_triggered:
        text = font.render("Combat", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(60)
