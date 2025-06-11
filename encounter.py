import pygame


class EncounterManager:
    """Manage encounter zones and return data about triggered encounters."""

    def __init__(self, game_map):
        self.tile_size = game_map.tile_size
       
        # Each encounter zone has a name so it can be displayed on the
        # transition screen.
        self.encounters = [
            (
                "Goblin",
                pygame.Rect(
                    18 * self.tile_size,
                    14 * self.tile_size,
                    self.tile_size,
                    self.tile_size,
                ),
            ),
            (
                "Slime",
                pygame.Rect(
                    10 * self.tile_size,
                    8 * self.tile_size,
                    self.tile_size,
                    self.tile_size,
                ),
            ),
        ]

    def check_trigger(self, player_rect):
        """Return the name of the encounter if the player collides."""

        for name, rect in self.encounters:
            if player_rect.colliderect(rect):
                return name
        return None

    def draw(self, surface):
        for name, rect in self.encounters:
            if name == "Slime":
                color = (0, 200, 0)  # Green
            else:
                color = (200, 0, 0)  # Red
            pygame.draw.rect(surface, color, rect)
