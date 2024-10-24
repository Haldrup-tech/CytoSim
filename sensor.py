import pygame

class Sensor:
  def __init__(self, width, distance, space):
    self.width = width
    self.distance = distance
    self.space = space
    self.volume =  width * pow(distance, 2)
    self.total_width = (4 * width) + space
    self.total_height = 100 * pow(10, -6) - distance
    
  def display(self, screenWidth, screenHeight, screen, scale):
    center_x = screenWidth / 2
    center_y = screenHeight / 2
    scaled_half_x = self.total_width / (2 * scale)
    scaled_half_y = self.total_height / (2 * scale)
    self.right_limit = center_x + scaled_half_x
    self.left_limit = center_x - scaled_half_x

    pygame.draw.line(screen, (255,255,255), (center_x - scaled_half_x, center_y - scaled_half_y), (center_x + scaled_half_x, center_y - scaled_half_y), 7)
    pygame.draw.line(screen, (255,255,255), (center_x + scaled_half_x, center_y - scaled_half_y), (center_x + scaled_half_x, center_y + scaled_half_y), 7)
    pygame.draw.line(screen, (255,255,255), (center_x + scaled_half_x, center_y + scaled_half_y), (center_x - scaled_half_x, center_y + scaled_half_y), 7)
    pygame.draw.line(screen, (255,255,255), (center_x - scaled_half_x, center_y + scaled_half_y), (center_x - scaled_half_x, center_y - scaled_half_y), 7)
    

    return 0 

  def testSensor1(self, partCenter, particle):
    if (particle.size >= abs(self.inner1 - (partCenter - particle.size))) and (particle.size >= abs(self.outer1 - (partCenter - particle.size))):
      volume = ((particle.volume / 2) - (particle.partialVol(particle.size - ((partCenter - particle.size) - self.inner1)))) + ((particle.volume / 2) - particle.partialVol(particle.size - (self.outer1 - (partCenter - particle.size)))) 
      return volume
    elif particle.size >= abs(self.inner1 - (partCenter - particle.size)):
      volume = particle.partialVol(particle.size - (self.inner1 - (partCenter - particle.size)))
      return volume
    elif particle.size >= abs(self.outer1 - (partCenter - particle.size)):
      volume = particle.volume - particle.partialVol(particle.size - (self.outer1 - (partCenter - particle.size)))
      return volume
    elif ((partCenter - particle.size) >= self.inner1 and (partCenter - particle.size) <= self.outer1):
      volume = particle.volume
      return volume
    else:
      return 0

  def testSensor2(self, partCenter, particle):
    if (particle.size >= abs(self.inner2 - (partCenter - particle.size))) and (particle.size >= abs(self.outer2 - (partCenter - particle.size))):
      volume = ((particle.volume / 2) - (particle.partialVol(particle.size - ((partCenter - particle.size) - self.inner2)))) + ((particle.volume / 2) - particle.partialVol(particle.size - (self.outer2 - (partCenter - particle.size)))) 
      return volume
    elif particle.size >= abs(self.inner2 - (partCenter - particle.size)):
      volume = particle.partialVol(particle.size - (self.inner2 - (partCenter - particle.size)))
      return volume
    elif particle.size >= abs(self.outer2 - (partCenter - particle.size)):
      volume = particle.volume - particle.partialVol(particle.size - (self.outer2 - (partCenter - particle.size)))
      return volume
    elif ((partCenter - particle.size) >= self.inner2 and (partCenter - particle.size) <= self.outer2):
      volume = particle.volume
      return volume
    else:
      return 0

  def getParticleVolume(self, partCenter, particle):
    volume1 = self.testSensor1(partCenter, particle)
    #volume1 = 0
    volume2 = self.testSensor2(partCenter, particle)

    if volume1:
      return volume1
    elif volume2:
      return volume2
    else:
      return 0
  
  def whichSensor(self, partCenter, particle):
    volume1 = self.testSensor1(partCenter, particle)
    #volume1 = 0
    volume2 = self.testSensor2(partCenter, particle)

    if volume1:
      return 1
    elif volume2:
      return 2
    else:
      return 0

  def inputVoltage(self, voltage1, voltage2):
    self.voltage1 = voltage1
    self.voltage2 = voltage2
