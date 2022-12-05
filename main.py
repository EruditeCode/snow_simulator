# Creating a snow simulator and exploring visualisation in Pygame.

import pygame
from class_Snowflake import Snowflake
from random import randint
from sys import exit

def main():
	# Initialising Pygame window, caption and clock.
	pygame.init()
	WIDTH, HEIGHT = 1080, 580
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Snow Simulation")
	clock = pygame.time.Clock()

	# Creating the image surfaces.
	trees_back = pygame.image.load('trees_back.jpg').convert_alpha()
	trees_front = pygame.image.load('trees_front.png').convert_alpha()

	# Create the snowflakes.
	snowflakes = []
	for i in range(0, 500):
		position = (randint(0, WIDTH), randint(0, HEIGHT))
		gravity = randint(1, 2)
		radius = randint(2, 4)
		snowflakes.append(Snowflake(position, radius, gravity))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		screen.blit(trees_back, (0, 0))		
		
		# Draw the snowflakes.
		for snowflake in snowflakes:
			snowflake.draw(screen)
			snowflake.controller(HEIGHT, WIDTH)

		screen.blit(trees_front, (0, 0))	

		pygame.display.update()
		clock.tick(30)
	

if __name__ == "__main__":
	main()
