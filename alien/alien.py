import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class that shows a single alien"""

	def __init__(self, ai_settings, screen):
		"""Initialize alien and set up its initial position"""
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen

		# Load the alien's image, and set up its rect attribute
		self.image = pygame.image.load('alien.bmp')
		self.rect = self.image.get_rect()

		# Each alien is on the top left corner initially
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the exact position of the alien
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw alien on the appointed position"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Move the aliens rightwardly"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		"""if aliens at the edge, return True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True






