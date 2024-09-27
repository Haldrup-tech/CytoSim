import pygame

class Sensor:
  def __init__(self, width, distance, space):
    self.width = width
    self.distance = distance
    self.space = space
    self.volume =  width * pow(distance, 2)
    
  def generate(self, screenWidth, screenHeight, screen):
    self.sensor1_x = (screenWidth / 2) - (self.space / 2) - self.width
    self.sensor1_y = 0
    self.sensor1_x_size = self.width
    self.sensor1_y_size = (screenHeight / 2) - (self.distance / 2)

    self.inner1 = self.sensor1_x
    self.outer1 = self.inner1 + self.width
    
    sensor1a = pygame.Rect(self.sensor1_x, self.sensor1_y, self.sensor1_x_size, self.sensor1_y_size)
    sensor1b = pygame.Rect(self.sensor1_x, self.sensor1_y + self.sensor1_y_size + self.distance, self.sensor1_x_size, self.sensor1_y_size)
    pygame.draw.rect(screen, (0, 0, 255), sensor1a)
    pygame.draw.rect(screen, (0, 0, 255), sensor1b)

    self.sensor2_x = (screenWidth / 2) + (self.space / 2)
    self.sensor2_y = 0
    self.sensor2_x_size = self.width
    self.sensor2_y_size = (screenHeight / 2) - (self.distance / 2)

    self.inner2 = self.sensor2_x
    self.outer2 = self.inner2 + self.width
    
    sensor2a = pygame.Rect(self.sensor2_x, self.sensor2_y, self.sensor2_x_size, self.sensor2_y_size)
    sensor2b = pygame.Rect(self.sensor2_x, self.sensor2_y + self.sensor2_y_size + self.distance, self.sensor2_x_size, self.sensor2_y_size)
    pygame.draw.rect(screen, (0, 0, 255), sensor2a)
    pygame.draw.rect(screen, (0, 0, 255), sensor2b)

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
