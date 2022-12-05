# A snowflake class to support the snow simulator program.

import pygame
from random import randint

class Snowflake:
	def __init__(self, position, radius, gravity):
		self.pos = position
		self.radius = radius
		self.gravity = gravity

	def draw(self, screen):
		pygame.draw.circle(screen, (250, 250, 250), self.pos, self.radius)


