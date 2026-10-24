# src/game.py
# done with ai since we dont know
# what to include to make the game run
# probably will change and adapt later

import pygame
import sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_BG, TITLE
from src.entities.player import Player
from src.managers.spawner import Spawner
from src.managers.collision import CollisionManager
from src.ui.hud import HUD


class Game:
	def __init__(self):
		# 1. Display Setup
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True

		# 2. Shared Sprite Groups
		self.all_sprites = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.projectiles = pygame.sprite.Group()
		self.pickups = pygame.sprite.Group()

		# 3. Instantiate Entities & Systems
		self.player = Player(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
		self.all_sprites.add(self.player)

		self.spawner = Spawner(self.all_sprites, self.enemies)
		self.collision_manager = CollisionManager(
			self.player, self.enemies, self.projectiles, self.pickups
		)
		self.hud = HUD(self.player)

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False

	def update(self, dt):
		# Update movement and internal timer logic across all active sprites
		self.all_sprites.update(dt)

		# Run system managers
		self.spawner.update(dt, self.player.rect.center)
		self.collision_manager.update()

	def render(self):
		# Clear screen with background color
		self.screen.fill(COLOR_BG)

		# Draw all active sprites
		self.all_sprites.draw(self.screen)

		# Draw UI overlay on top
		self.hud.draw(self.screen)

		# Flip display buffers
		pygame.display.flip()

	def run(self):
		while self.running:
			# Calculate delta time in seconds (e.g., 0.016s at 60 FPS)
			dt = self.clock.tick(FPS) / 1000.0

			self.handle_events()
			self.update(dt)
			self.render()