import math

class Particle:
  def __init__(self, speed, size, perm, rest):
    self.speed = speed
    self.size = size
    self.perm = perm
    self.rest = rest
    self.volume = (4/3.0) * math.pi * size * size * size 

  def move(self, time):
    distance = self.speed * time
    return distance

  def partialVol(self, height):
    partialVol = (1/3) * math.pi * height * height * ((3 * self.size) - height)
    return partialVol

  def updateSize(self, size):
    self.size = size
    self.volume = (4/3) * math.pi * size * size * size


