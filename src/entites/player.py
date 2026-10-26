import pygame
from src.settings import PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, DASH_SPEED
from src.entites.weapons import BaseWeapon, MagicWand, Slash, Meteorite

# trial and error
PLAYER_IMG_HEIGHT = 60
PLAYER_IMG_WIDTH = 40


# pretty much just java code from this point on
class Player(pygame.sprite.Sprite):

	# changed "this" to "self"

	# initialization
	def __init__(self, pos):
		super().__init__()

		#########################################

		# convert_alpha() is for png to be a png and not a box
		# well, if it was actually a png
		raw_image = pygame.image.load('assets/images/player_placeholder.png').convert_alpha()
		self.image = pygame.transform.scale(raw_image, (PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT))


		self.rect = self.image.get_rect(center=pos)
		self.rect = self.image.get_rect(center=pos)

		#########################################
		#  ^
		#  |  yay first merge conflict
		#  |

		self.pos = pygame.math.Vector2(pos)
		self.speed = PLAYER_SPEED

		# self.weapons = []
		# self.add_weapon(MagicWand(self))

		#dash related variables
		self.is_dashing = False
		self.last_dash_time = 0
		self.is_invincible = False
		self.dash_dx = 0
		self.dash_dy = 0
		self.dash_duration = 100
		self.dash_cooldown = 1000

	# def add_weapon(self, weapon: BaseWeapon):
	# 	self.weapons.append(weapon)

	def get_input(self):
		keys = pygame.key.get_pressed()
		direction = pygame.math.Vector2(0, 0)

		current_time = pygame.time.get_ticks()

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


		#sets dash direction
		if direction != (0,0):
			self.dash_dx = direction.x
			self.dash_dy = direction.y

		if keys[pygame.K_LSHIFT] and not self.is_dashing:
			if current_time - self.last_dash_time >= self.dash_cooldown: #time elapsed > cooldown
				self.is_dashing = True
				self.is_invincible = True
				self.last_dash_time = current_time

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

	def update(self, dt):
		direction = self.get_input()
		current_time = pygame.time.get_ticks()

		if self.is_dashing:
			# if dash ends
			if current_time - self.last_dash_time >= self.dash_duration:
				self.is_dashing = False
				self.is_invincible = False
				self.speed = PLAYER_SPEED
			else:
				# if dash started or still is in effect
				direction.x = self.dash_dx
				direction.y = self.dash_dy
				self.speed = DASH_SPEED


		# first time writing this line managed
		# to achieve the speed of light (forgot dt)
		self.pos += direction * self.speed * dt
		self.rect.center = (round(self.pos.x), round(self.pos.y))

		self.no_offscreen_warriors()


		# if all_sprites is not None and projectile_group is not None and enemy_group is not None:
		# 	for weapon in self.weapons:
		# 		weapon.update(all_sprites, projectile_group, enemy_group)