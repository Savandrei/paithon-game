import pygame
from .base_weapon import BaseWeapon
from src.entites.projectiles import Bullet

class MagicWand(BaseWeapon):
    # Auto-fires a bullet at the nearest enemy on a set cooldown
    def __init__(self, player):
        super().__init__(player, cooldown_frames=45) 

    def attack(self, all_sprites, projectile_group, enemy_group):
        if not enemy_group:
            return

        # Locate the closest enemy relative to the player
        closest_enemy = min(
            enemy_group.sprites(),
            key=lambda e: pygame.math.Vector2(self.player.rect.center).distance_to(e.rect.center)
        )

        # Calculate the firing trajectory
        direction = pygame.math.Vector2(closest_enemy.rect.center) - self.player.rect.center

        # Spawn the bullet and assign it to the groups
        bullet = Bullet(pos=self.player.rect.center, direction=direction)
        all_sprites.add(bullet)
        projectile_group.add(bullet)