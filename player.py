import pygame

TILE_SIZE = 32

class Player:
    def __init__(self, position):
        # Load and scale sprites to tile size
        self.sprite_right = pygame.transform.scale(
            pygame.image.load("assets/knight_right.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.sprite_back = pygame.transform.scale(
            pygame.image.load("assets/knight_back.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.sprite_front = pygame.transform.scale(
            pygame.image.load("assets/knight_front.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        
        self.rect = self.sprite_right.get_rect(center=position)
        self.speed = 4
        self.facing = "right"

    def update(self, keys, game_map):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
            self.facing = "left"
        elif keys[pygame.K_RIGHT]:
            dx = self.speed
            self.facing = "right"
        if keys[pygame.K_UP]:
            dy = -self.speed
            self.facing = "up"
        elif keys[pygame.K_DOWN]:
            dy = self.speed
            self.facing = "down"

        # Move horizontally and check collisions using the full rect
        if dx != 0:
            new_rect = self.rect.move(dx, 0)
            if game_map.is_rect_walkable(new_rect):
                self.rect = new_rect

        # Move vertically and check collisions using the updated rect
        if dy != 0:
            new_rect = self.rect.move(0, dy)
            if game_map.is_rect_walkable(new_rect):
                self.rect = new_rect


        # Ensure the player stays within the screen bounds
        screen_bounds = pygame.Rect(0, 0, 640, 480)
        self.rect.clamp_ip(screen_bounds)

    def draw(self, surface):
        if self.facing == "right":
            sprite = self.sprite_right
        elif self.facing == "left":
            sprite = pygame.transform.flip(self.sprite_right, True, False)
        elif self.facing == "up":
            sprite = self.sprite_back
        elif self.facing == "down":
            sprite = self.sprite_front
        surface.blit(sprite, self.rect)
