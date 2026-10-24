from .base_enemy import BaseEnemy

class Zombie(BaseEnemy):
    def __init__(self, pos, target_player):
        # We pass the specific stats for a Zombie into your BaseEnemy's __init__
        super().__init__(
            pos=pos,
            target_player=target_player,
            speed=1.2,
            health=80,
            damage=20,
            color=(50, 180, 75),  # Green color
            size=(32, 32)
        )