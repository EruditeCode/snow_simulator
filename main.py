# Creating a snow simulator and exploring visualisation in Pygame.

import pygame
from random import randint
from sys import exit

class Snowflake:
	def __init__(self, position, radius, gravity):
		self.pos = position
		self.RADIUS_MAX = radius
		self.radius = radius
		self.gravity = gravity
		self.radius_change = True

	def controller(self, height, width):
		self.update_pos(height, width)

		if self.radius_change:
			self.update_rad()
			self.radius_change = False
		else:
			self.radius_change = True

	def update_pos(self, height, width):
		if self.pos[1] < height + self.radius:
			self.pos = (self.pos[0] + randint(-1, 1), self.pos[1] + self.gravity)
		else:
			self.respawn(width)

	def update_rad(self):
		self.radius = randint(1, self.RADIUS_MAX)

	def respawn(self, width):
		self.pos = (randint(0, width), -1 * self.radius)

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
		
		# Draw the snowflakes. (255, 251, 251)
		for snowflake in snowflakes:
			pygame.draw.circle(screen, (200, 200, 200), snowflake.pos, snowflake.radius)
			snowflake.controller(HEIGHT, WIDTH)

		screen.blit(trees_front, (0, 0))	

		pygame.display.update()
		clock.tick(30)
	

if __name__ == "__main__":
	main()
