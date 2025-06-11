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

# Track the current game state. Possible values:
# 'overworld' - walking around the map
# 'encounter' - short intro scene before combat
# 'combat'    - combat mode (placeholder)
game_state = "overworld"

# When entering an encounter these variables are set
current_enemy = None
encounter_start = 0

# Game objects
game_map = GameMap()
player = Player((200, 64))  # Placed on a walkable tile

# Encounter manager handles encounter zones and collisions
encounters = EncounterManager(game_map)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Allow returning to overworld from combat with Escape key
        if game_state == "combat" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "overworld"

    if game_state == "overworld":
        keys = pygame.key.get_pressed()
        player.update(keys, game_map)

        encounter_trigger = encounters.check_trigger(player.rect)
        if encounter_trigger:
            game_state = "encounter"
            current_enemy = encounter_trigger
            encounter_start = pygame.time.get_ticks()

        screen.fill((30, 30, 30))
        game_map.draw(screen)
        encounters.draw(screen)
        player.draw(screen)

    elif game_state == "encounter":
        screen.fill((0, 0, 0))

        # Enemy rectangle and name at the top right
        enemy_rect = pygame.Rect(screen.get_width() - 84, 20, 64, 64)

        # Display the correct enemy sprite
        if current_enemy == "Slime":
            enemy_sprite = encounters.slime_sprite
        elif current_enemy == "Goblin":
            enemy_sprite = pygame.Surface((64, 64))  # Placeholder for Goblin sprite
            enemy_sprite.fill((200, 0, 0))  # Red rectangle for Goblin
        else:
            enemy_sprite = pygame.Surface((64, 64))  # Default placeholder
            enemy_sprite.fill((100, 100, 100))  # Gray rectangle for unknown enemies

        screen.blit(enemy_sprite, enemy_rect.topleft)

        # Display the enemy name below the sprite
        name_surface = font.render(current_enemy, True, (255, 255, 255))
        screen.blit(
            name_surface,
            (
                screen.get_width() - name_surface.get_width() - 20,
                enemy_rect.bottom + 5,
            ),
        )

        # Draw the player sprite in the bottom left
        if player.facing == "right":
            sprite = player.sprite_right
        elif player.facing == "left":
            sprite = pygame.transform.flip(player.sprite_right, True, False)
        elif player.facing == "up":
            sprite = player.sprite_back
        else:
            sprite = player.sprite_front
        screen.blit(sprite, (20, screen.get_height() - sprite.get_height() - 20))

        if pygame.time.get_ticks() - encounter_start >= 5000:
            game_state = "combat"

    elif game_state == "combat":
        screen.fill((0, 0, 0))
        combat_text = font.render("Combat Mode", True, (255, 255, 255))
        screen.blit(
            combat_text,
            (
                screen.get_width() // 2 - combat_text.get_width() // 2,
                screen.get_height() // 2 - combat_text.get_height() // 2,
            ),
        )

    pygame.display.flip()
    clock.tick(60)
