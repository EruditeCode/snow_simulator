# A snowflake class to support the snow simulator program.

import pygame
from random import randint

class Snowflake:
	def __init__(self, position, radius, gravity):
		self.pos = position
		self.radius = radius
		self.gravity = gravity

	def controller(self, height, width):
		self.update_pos(height, width)

	def update_pos(self, height, width):
		if self.pos[1] < height + self.radius:
			self.pos = (self.pos[0] + randint(-1, 1), self.pos[1] + self.gravity)
		else:
			self.respawn(width)

	def respawn(self, width):
	 	self.pos = (randint(0, width), -1 * self.radius)

	def draw(self, screen, height):
		rgb = 250 - 100 * (self.pos[1] / height) 
		color = (rgb, rgb, rgb)
		pygame.draw.circle(screen, color, self.pos, self.radius)


