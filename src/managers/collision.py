import pygame

class CollisionManager:
    # Handles spatial overlaps and combat interactions between game entities

    def __init__(self, player, enemy_group, projectile_group, pickup_group):
        self.player = player
        self.enemy_group = enemy_group
        self.projectile_group = projectile_group
        self.pickup_group = pickup_group

    def update(self):
        self._handle_combat_collisions()
        # self._handle_pickups()  # To be implemented when we add XP gems

    def _handle_combat_collisions(self):
        # 1. Projectiles vs Enemies
        # groupcollide returns a dict: {Projectile: [Hit_Enemy_1, Hit_Enemy_2, ...]}
        hits = pygame.sprite.groupcollide(self.projectile_group, self.enemy_group, False, False)
        
        for bullet, hit_enemies in hits.items():
            for enemy in hit_enemies:
                # Deal damage to the enemy
                enemy.take_damage(bullet.damage)
                
                # Reduce bullet pierce count
                bullet.hit_enemy()
                
                # If the bullet was destroyed (pierce depleted), stop checking it against others
                if not bullet.alive():
                    break

        # 2. Enemies vs Player
        # spritecollide returns a list of enemies currently touching the player
        collided_enemies = pygame.sprite.spritecollide(self.player, self.enemy_group, False)

        for enemy in collided_enemies:
            # Assumes your partner's Player class has a take_damage method with i-frames
            self.player.take_damage(enemy.damage)
            # game doesn't know what to do if an enemy touches the player and the game will crash
            # solution? just don't get hit