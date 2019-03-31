import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" A class that manages bullets shot by the ship"""

	def __init__(self, screen, ai_settings, ship):
		""" Create an object in the position of the ship"""
		super().__init__()
		self.screen = screen

		# Create a rectangle of the bullet at (0, 0), and set up the correct position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store bullet position in fraction
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		""" Move the bullet upwardly"""
		# Update the fraction of bullet's position
		self.y -= self.speed_factor
		# Update position of bullet's rect
		self.rect.y = self.y

	def draw_bullet(self):
		""" Draw the bullet on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)