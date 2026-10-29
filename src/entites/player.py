import pygame
import os
from src.settings import PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

# trial and error
PLAYER_IMG_HEIGHT = 60
PLAYER_IMG_WIDTH = 40


# pretty much just java code from this point on
class Player(pygame.sprite.Sprite):

	# changed "this" to "self"

	# initialization
	def __init__(self, pos):
		super().__init__()

		# convert_alpha() is for png to be a png and not a box
		# well, if it was actually a png
		raw_image = pygame.image.load('paithon-game/assets/images/player_placeholder.png').convert_alpha()
		self.image = pygame.transform.scale(raw_image, (PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT))


		self.rect = self.image.get_rect(center=pos)
		self.rect = self.image.get_rect(center=pos)

		self.pos = pygame.math.Vector2(pos)
		self.speed = PLAYER_SPEED

	def get_input(self):
		keys = pygame.key.get_pressed()
		direction = pygame.math.Vector2(0, 0)

		# arrow movement
		if keys[pygame.K_UP]:
			direction.y -= 1
		if keys[pygame.K_DOWN]:
			direction.y += 1
		if keys[pygame.K_LEFT]:
			direction.x -= 1
		if keys[pygame.K_RIGHT]:
			direction.x += 1

		# wasd movement
		if keys[pygame.K_w]:
			direction.y -= 1
		if keys[pygame.K_s]:
			direction.y += 1
		if keys[pygame.K_a]:
			direction.x -= 1
		if keys[pygame.K_d]:
			direction.x += 1

		return direction

	def no_offscreen_warriors(self):
		self.rect.left = max(0, self.rect.left)
		self.rect.right = min(SCREEN_WIDTH, self.rect.right)
		self.rect.top = max(0, self.rect.top)
		self.rect.bottom = min(SCREEN_HEIGHT, self.rect.bottom)


		# I would debug for hours bcuz I forgot abt this
		# thx ai
		self.pos.x = self.rect.centerx
		self.pos.y = self.rect.centery

	def update(this, dt):
		direction = this.get_input()


		# first time writing this line managed
		# to achieve the speed of light (forgot dt)
		this.pos += direction * this.speed * dt
		this.rect.center = (round(this.pos.x), round(this.pos.y))

		this.no_offscreen_warriors()