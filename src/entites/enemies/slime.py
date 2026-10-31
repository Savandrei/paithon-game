from .base_enemy import BaseEnemy

class Slime(BaseEnemy):
    """A bouncy, medium-health enemy."""
    def __init__(self, pos, target_player):
        super().__init__(
            pos=pos,
            target_player=target_player,
            speed=180,
            health=40,
            damage=10,
            color=(0, 200, 100),  # Slime Green
            size=(20, 20)
        )