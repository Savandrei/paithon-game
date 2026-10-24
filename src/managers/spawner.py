import random
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from src.entites.enemies import Bat, Zombie

class Spawner:
    """
    Handles spawning enemies outside the camera view at set intervals.
    """
    def __init__(self, all_sprites, enemy_group, target_player):
        self.all_sprites = all_sprites
        self.enemy_group = enemy_group
        self.target = target_player
        
        # Timing and progression
        self.timer = 0
        self.spawn_interval = 45  # Frames between each spawn

    def get_perimeter_pos(self):
        """Calculates a random coordinate just outside the screen boundaries."""
        side = random.choice(["top", "bottom", "left", "right"])
        offset = 50  # Spawn 50 pixels off-screen so they don't pop in
        
        if side == "top":
            return random.randint(0, SCREEN_WIDTH), -offset
        elif side == "bottom":
            return random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + offset
        elif side == "left":
            return -offset, random.randint(0, SCREEN_HEIGHT)
        else: # right
            return SCREEN_WIDTH + offset, random.randint(0, SCREEN_HEIGHT)

    def update(self, dt):
        """Ticks the spawn timer and creates enemies."""
        self.timer += 1
        
        if self.timer >= self.spawn_interval:
            self.timer = 0
            pos = self.get_perimeter_pos()
            
            # Weighted random choice: 70% chance for Bat, 30% chance for Zombie
            enemy_class = random.choices([Bat, Zombie], weights=[70, 30])[0]
            
            # Instantiate the chosen enemy and add to groups
            enemy = enemy_class(pos=pos, target_player=self.target)
            self.all_sprites.add(enemy)
            self.enemy_group.add(enemy)