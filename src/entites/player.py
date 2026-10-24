import pygame
import os
from src.settings import PLAYER_SPEED

# pretty much just java code from this point on
class Player(pygame.sprite.Sprite):

	# initialization
	def __init__(this, pos):
		super().__init__()

		this.image = pygame.image.load('paithon-game/assets/images/player_placeholder.png')
		this.rect = this.image.get_rect(center=pos)

		this.pos = pygame.math.Vector2(pos)
		this.speed = PLAYER_SPEED

	def get_input(this):
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

	def update(this, dt):
		direction = this.get_input()

		this.pos += direction * this.speed * dt
		this.rect.center = (round(this.pos.x), round(this.pos.y))