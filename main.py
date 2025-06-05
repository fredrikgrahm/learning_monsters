import pygame
import sys
from player import Player
from map import GameMap 

# Init
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Learning Monsters")
clock = pygame.time.Clock()

# Game objects
game_map = GameMap()
player = Player((200, 64))  # Placed on a walkable tile

# Game loop
while True:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.update(keys, game_map)

    # Draw map and player
    game_map.draw(screen)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)
