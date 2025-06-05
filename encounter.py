import pygame

class EncounterManager:
    def __init__(self, game_map):
        self.tile_size = game_map.tile_size
        self.encounter_positions = [
            (18 * self.tile_size, 14 * self.tile_size),
            (10 * self.tile_size, 8 * self.tile_size),
        ]
        self.encounter_rects = [
            pygame.Rect(pos, (self.tile_size, self.tile_size))
            for pos in self.encounter_positions
        ]

    def check_trigger(self, player_rect):
        return any(player_rect.colliderect(rect) for rect in self.encounter_rects)

    def draw(self, surface):
        for rect in self.encounter_rects:
            pygame.draw.rect(surface, (200, 0, 0), rect)