import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, screen, ai_settings):
		"""Initialize ship and set up its initial position"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load ship image and capture its envelop rectangle
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Place every new ship in the middle of the bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store fraction in the 'center' of the ship settings
		self.center = float(self.rect.centerx)

		# Moving sign
		self.moving_right = False
		self.moving_left = False

	def update(self):
		""" Modify the ship's position according to moving sign"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center 

	def blitme(self):
		"""Draw the ship on the appointed position"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship"""
		self.center = self.screen_rect.centerx


