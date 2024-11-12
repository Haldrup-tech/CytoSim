import math
import pygame

class Particle:
  def __init__(self, speed, size, perm, rest):
    self.speed = speed
    self.size = size
    self.radius = size / 2
    self.perm = perm
    self.rest = rest
    self.volume = (4/3.0) * math.pi * pow(self.radius, 3) 
    self.distance = 0

  def move(self, time_interval, scale, left_limit, right_limit, screen, height):
    self.distance += (self.speed * time_interval) / scale
    self.pixel_distance = self.distance + left_limit
    if self.distance + left_limit + (self.size / (2 * scale)) > right_limit:
      self.distance = 0
    pygame.draw.circle(screen, (255,225,255), (left_limit + self.distance, height / 2), self.size / (2 * scale))

  def partialVol(self, height):
    partialVol = (1/3) * math.pi * height * height * ((3 * self.size) - height)
    return partialVol

  def updateSize(self, size):
    self.size = size
    self.volume = (4/3) * math.pi * size * size * size


