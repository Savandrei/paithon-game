import pygame
from .base_projectile import BaseProjectile

class BlastVisual(BaseProjectile):
    """A visual-only explosion indicator that deals no direct projectile damage."""
    def __init__(self, pos, radius):
        super().__init__(
            pos=pos,
            direction=pygame.math.Vector2(1, 0),
            speed=0,
            damage=0, 
            pierce=0,
            lifetime=15,
            color=(255, 100, 0), 
            size=(radius * 2, radius * 2)
        )