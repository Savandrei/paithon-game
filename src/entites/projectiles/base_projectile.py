import pygame

from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class BaseProjectile(pygame.sprite.Sprite):
    # Base class for all flying attacks/projectiles
    def __init__(
        self,
        pos,
        direction,
        speed=7.0,
        damage=15,
        pierce=1,
        lifetime=120,
        color=(255, 220, 50),
        size=(10, 10),
    ):
        super().__init__()

        # Visual representation (placeholder circle until sprite assets are hooked up)
        self.size = size
        self.color = color
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.circle(
            self.image,
            self.color,
            (size[0] // 2, size[1] // 2),
            size[0] // 2,
        )
        self.rect = self.image.get_rect(center=pos)

        # High-precision vector coordinates
        self.pos = pygame.math.Vector2(pos)
        
        # Ensure direction is a unit vector
        if direction.length_squared() > 0:
            self.direction = direction.normalize()
        else:
            self.direction = pygame.math.Vector2(1, 0)

        # Combat & lifecycle stats
        self.speed = speed
        self.damage = damage
        self.pierce = pierce
        self.lifetime = lifetime

    def update(self):
        # Move forward and check expiration
        self.move()
        self.check_lifetime_and_bounds()

    def move(self):
        # Advances position along direction vector
        self.pos += self.direction * self.speed
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def check_lifetime_and_bounds(self):
        # Despawns projectile if its timer runs out or it leaves the screen
        self.lifetime -= 1
        screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        if self.lifetime <= 0 or not screen_rect.colliderect(self.rect):
            self.kill()

    def hit_enemy(self):
        # Decreases pierce count upon hitting an enemy
        self.pierce -= 1
        if self.pierce <= 0:
            self.kill()