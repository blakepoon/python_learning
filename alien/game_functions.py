import sys
import time
import pygame
import json
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ship, ai_settings, screen, bullets, stats, aliens, sb):
	"""Response to keydown"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(screen, ai_settings, ship, bullets)
	elif event.key == pygame.K_p and not stats.game_active:
		start_game(ai_settings, screen, stats, aliens, bullets, ship, sb)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	"""Response to keyup"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ship, ai_settings, screen, bullets, play_button, stats, aliens, sb):
	""" Response to keyboard and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship, ai_settings, screen, bullets, stats, aliens, sb)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, aliens, ship, play_button, stats, 
				bullets, mouse_x, mouse_y, sb)

def update_screen(screen, ship, ai_settings, bullets, aliens, stats, play_button, sb):

	#Reset the screen for every loop
	screen.fill(ai_settings.bg_color)
	# Redraw all bullets after ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	# Display the score
	sb.show_score()

	# If the game is inactive, draw the Play button
	if not stats.game_active:
		play_button.draw_button()
	
	#Be visible to recently drawn screen
	pygame.display.flip()

def update_bullets(bullets, aliens, ai_settings, screen, ship, stats, sb):
	"""Update bullet's position and delete the gone bullet"""
	# Update bullet's position
	bullets.update()
	# Delete the gone bullet
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)

def fire_bullet(screen, ai_settings, ship, bullets):
	"""shoot a bullet if within the limit"""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(screen, ai_settings, ship)
		bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
	"""Create an alien and calculate how many aliens can be accommodated per row""" 
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_row(ai_settings, ship_height, alien_height):
	"""Calculate how many rows of aliens can be accommodated within the screen"""
	available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	# Create an alien and add it onto current row
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien_height + 2 * alien_height * row_number
	aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
	"""Create a fleet of aliens"""
	# Interval is the width of alien
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_row(ai_settings, ship.rect.height, alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
	"""Execute certain steps while aliens hit the edges"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""Move the whole fleet down and change the direction"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def update_aliens(stats, bullets, ai_settings, screen, aliens, ship, sb):
	"""Update the positions of all aliens in the fleet"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	# Detect collisions between aliens and the ship
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(stats, bullets, ai_settings, screen, aliens, ship, sb)
	# see if any aliens reaching the bototm
	check_aliens_bottom(stats, bullets, ai_settings, screen, aliens, ship, sb)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
	# Check if any bullets hitting aliens
	# If so delete the bullet and the alien
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		# Delete the existent bullets, speed up the game, and create new fleet of aliens
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, aliens, ship)

		# level up if the whole fleet terminated
		stats.level += 1
		sb.prep_level()

	if collisions:
		for aliens in collisions.values():
				stats.score += ai_settings.alien_points * len(aliens)
				sb.prep_score()
				check_high_score(stats, sb)

def ship_hit(stats, bullets, ai_settings, screen, aliens, ship, sb):
	"""Response to ship hit by aliens"""
	if stats.ships_left > 1:
		# Subtract ships_left by 1
		stats.ships_left -= 1

		# Empty list of aliens and bullets
		aliens.empty()
		bullets.empty()

		# Create a new fleet of aliens and place the ship in the middle of the bottom
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()

		# Update the score
		sb.prep_ship()

		# Pause
		time.sleep(0.5)

	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(stats, bullets, ai_settings, screen, aliens, ship, sb):
	"""Check if any aliens reaching the bottom"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Processed as the ship gets hit
			ship_hit(stats, bullets, ai_settings, screen, aliens, ship, sb)
			break

def check_play_button(ai_settings, screen, aliens, ship, play_button, stats, 
		bullets, mouse_x, mouse_y, sb):
	"""Begin a new game while players click the play button"""
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		start_game(ai_settings, screen, stats, aliens, bullets, ship, sb)
		ai_settings.initialize_dynamic_settings()

def start_game(ai_settings, screen, stats, aliens, bullets, ship, sb):
	"""Reset the stats and start the game"""
	# Hide the cursor
	pygame.mouse.set_visible(False)
	stats.reset_stats()
	sb.prep_score()
	sb.prep_level()
	sb.prep_ship()
	stats.game_active = True

	# Empty the list of aliens and list of bullets
	aliens.empty()
	bullets.empty()

	# Creat a new fleet of aliens and center the ship
	create_fleet(ai_settings, screen, aliens, ship)
	ship.center_ship()

def check_high_score(stats, sb):
	"""see if highest score coming up"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

		# Store the highest score in json
		with open(stats.high_score_data, 'w') as h:
			json.dump(stats.score, h)









