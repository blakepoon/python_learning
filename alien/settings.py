class Settings():
	"""Store all classes for settings in 'Alien Invasion'"""

	def __init__(self):
		"""Settings for initializing the game"""
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_limit = 3

		# Bullet Settings

		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10

		# Alien settings
		self.fleet_drop_speed = 20

		# with what speed to accelerate the game
		self.speedup_scale = 1.1
		# with what speed to increase the score per alien
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize setting changing along with the game proceeding"""
		self.ship_speed_factor = 20
		self.bullet_speed_factor = 10
		self.alien_speed_factor = 50

		# Fleet direction: 1 for right; -1 for left
		self.fleet_direction = 1

		# Score
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed setting"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)









