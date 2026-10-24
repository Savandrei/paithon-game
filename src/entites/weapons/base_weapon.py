import pygame


class BaseWeapon:
    """
    Base class for player weapons and abilities.
    Tracks cooldown timers, weapon level, and triggers attacks.
    """
    def __init__(self, player, cooldown_frames=45):
        self.player = player
        self.cooldown_frames = cooldown_frames
        self.timer = 0
        self.level = 1

    def update(self, all_sprites, projectile_group, enemy_group):
        """
        Ticks the weapon cooldown every frame.
        Fires attack() when cooldown elapses.
        """
        self.timer += 1
        if self.timer >= self.cooldown_frames:
            self.timer = 0
            self.attack(all_sprites, projectile_group, enemy_group)

    def attack(self, all_sprites, projectile_group, enemy_group):
        """
        Subclasses must override this method with specific targeting
        and projectile spawning logic.
        """
        raise NotImplementedError("Each weapon subclass must implement attack().")

    def level_up(self):
        """Increases weapon rank and boosts stats (cooldown, damage, etc.)."""
        self.level += 1
        # Example default progression: fire slightly faster with each level
        self.cooldown_frames = max(10, int(self.cooldown_frames * 0.9))