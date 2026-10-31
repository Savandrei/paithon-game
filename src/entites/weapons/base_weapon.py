import pygame

class BaseWeapon:
    # Base class for player weapons and abilities
    # Tracks cooldown timers in seconds, weapon level, and triggers attacks
    def __init__(self, player, cooldown=0.75, projectile_number=1):
        self.player = player
        self.cooldown = cooldown
        self.timer = 0.0
        self.level = 1
        self.projectile_number = projectile_number

    def update(self, dt, all_sprites, projectile_group, enemy_group):
        # Ticks the weapon cooldown using delta time (in seconds)
        # Fires attack() when cooldown elapses
        self.timer += dt
        if self.timer >= self.cooldown:
            self.timer = 0.0
            self.attack(all_sprites, projectile_group, enemy_group)

    def attack(self, all_sprites, projectile_group, enemy_group):
        # This is going to get overridden by the subclasses
        raise NotImplementedError("Each weapon subclass must implement attack().")

    def level_up(self):
        # Increases weapon rank and boosts stats (cooldown, damage, etc.)
        self.level += 1
        # Example default progression: fire slightly faster with each level (10% reduction)
        self.cooldown = max(0.15, self.cooldown * 0.9)