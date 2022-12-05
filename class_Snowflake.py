# A snowflake class to support the snow simulator program.

import pygame
from random import randint

class Snowflake:
	def __init__(self, position, radius, gravity):
		self.pos = position
		self.radius = radius
		self.gravity = gravity
		self.RADIUS_MAX = radius
		self.radius_change = True

	def controller(self, height, width):
		self.update_pos(height, width)
		self.update_rad()

	def update_pos(self, height, width):
		if self.pos[1] < height + self.radius:
			self.pos = (self.pos[0] + randint(-1, 1), self.pos[1] + self.gravity)
		else:
			self.respawn(width)

	def update_rad(self):
		if self.radius_change:
			self.radius = randint(1, self.RADIUS_MAX)
			self.radius_change = False
		else:
			self.radius_change = True

	def respawn(self, width):
	 	self.pos = (randint(0, width), -1 * self.radius)

	def draw(self, screen, height):
		rgb = 250 - 100 * (self.pos[1] / height) 
		color = (rgb, rgb, rgb)
		pygame.draw.circle(screen, color, self.pos, self.radius)


