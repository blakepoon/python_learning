import json

class GameStats():
	"""Trace the game stats"""

	def __init__(self, ai_settings):
		"""Initialize game stats"""
		self.ai_settings = ai_settings
		self.reset_stats()
		# game is inactive while starting
		self.game_active = False
		self.score = 0
		# Under no circumstances should the highest score be reset
		self.open_json()

	def reset_stats(self):
		"""Initialize the game stats potentially changing during the game"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

	def open_json(self):
		"""Open the highest_score stored in json"""
		self.high_score_data = 'high_score.json'	
		with open(self.high_score_data) as h:
			self.high_score = json.load(h)
