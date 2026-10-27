import pygame
from .base_projectile import BaseProjectile

class Bullet(BaseProjectile):
	# A standard yellow projectile that hits a single target
	def __init__(self, pos, direction):
		super().__init__(
			pos=pos,
			direction=direction,
			speed=600,
			damage=15,
			pierce=1,
			lifetime=120,
			color=(255, 220, 50),
			size=(40, 20)
		)

		# outer layer
		pygame.draw.rect(self.image, (0, 0, 0, 100), (0, 0, 40, 20))
		# inner layer(with color)
		pygame.draw.rect(self.image, (255, 220, 50), (5, 5, 30, 10))

		# rotation
		if self.direction != (0,0):
			# as_polar returns (length, angle_in_degrees)
			# Pygame's Y-axis is inverted (0 is at the top)
			angle = -self.direction.as_polar()[1]
			self.image = pygame.transform.rotate(self.image, angle)
			self.rect = self.image.get_rect(center=self.rect.center)

		self.rotated_image = self.image.copy()

	def update(self, dt, *args, **kwargs):
		# the base_projectile shrinked one dimension of the bullet
		return_value = super().update(dt, *args, **kwargs)
		self.image = self.rotated_image
		return return_value