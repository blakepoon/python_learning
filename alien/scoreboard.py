import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""Class showing the score"""
	def __init__(self, ai_settings, screen, stats):
		"""Initialize the attribute concerning the score"""
		self.ai_settings = ai_settings
		self.screen = screen
		self.stats = stats
		self.screen_rect = screen.get_rect()

		# Font setting for score display
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# Prepare initial score image and highest score
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ship()

	def prep_score(self):
		"""Convert the score to a rendered image"""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, 
			self.ai_settings.bg_color)

		# Place the score on the right of the top
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""Display the score and highest score on the screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		# Draw ships
		self.ships.draw(self.screen)

	def prep_high_score(self):
		"""Convert the highest score to rendered image"""
		rounded_high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(rounded_high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, 
			self.ai_settings.bg_color)

		# Place the high score in the center of the top
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = 20

	def prep_level(self):
		"""Convert the level to rendered image"""
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, 
			self.ai_settings.bg_color)

		# Place the level under the score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ship(self):
		"""Display how many ships left"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.screen, self.ai_settings)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)





