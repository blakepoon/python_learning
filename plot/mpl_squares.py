import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
	#Initialize the game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Create a ship
	ship = Ship(screen, ai_settings)

	# Create a group used to store the bullets
	bullets = Group()

	# Create a group of aliens
	aliens = Group()

	# Create a fleet of alien
	gf.create_fleet(ai_settings, screen, aliens, ship)

	# Create an instance storing the game stats and create a scoreboard
	stats = GameStats(ai_settings) 
	sb = Scoreboard(ai_settings, screen, stats)

	# Create a Play button
	play_button = Button(ai_settings, screen, 'Play')


	#Begin main loop of the game
	while True:
		gf.check_events(ship, ai_settings, screen, bullets, play_button, stats, aliens, sb)

		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, ai_settings, screen, ship, stats, sb)
			gf.update_aliens(stats, bullets, ai_settings, screen, aliens, ship, sb)
			
		gf.update_screen(screen, ship, ai_settings, bullets, aliens, stats, play_button, sb)


run_game()

"""endgame"""