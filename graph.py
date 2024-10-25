import pygame

class Graph:
	def __init__(self, ratio, max_time, center, y_scale):
		self.ratio = ratio
		self.max_time = max_time
		self.center = center
		self.y_scale = y_scale
		self.data = []

	def draw(self, screen, x, y, time_scale):
		rect = pygame.Rect(0, 0, x, y / self.ratio)
		pygame.draw.rect(screen, (0,0,0), rect)
		self.draw_data(x, y, screen, time_scale)

	def add_data(self, time, value):
		self.data.append([time, value])

	def get_data(self):
		return self.data

	def draw_data(self, x, y, screen, time_scale):
		offset = 0
		for i in range(len(self.data) - 1, -1, -1):
			pygame.draw.circle(screen, (255,0,0), (x - offset ,(y / (2 * self.ratio)) + self.data[i][1] * 10), 1)
			offset += time_scale * 10