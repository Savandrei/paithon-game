from .base_projectile import BaseProjectile

class Bullet(BaseProjectile):
    """A standard yellow projectile that hits a single target."""
    def __init__(self, pos, direction):
        super().__init__(
            pos=pos,
            direction=direction,
            speed=7.5,
            damage=15,
            pierce=1,
            lifetime=120,
            color=(255, 220, 50),
            size=(10, 10)
        )