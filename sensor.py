import pygame
import math

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
    scaled_width = self.width / scale
    scaled_distance = self.distance / scale
    scaled_space = self.space / scale
    self.height = screenHeight

    self.scaled_sensor1_left_limit = center_x - scaled_space - scaled_width 
    self.scaled_sensor1_right_limit = center_x - scaled_space 
    self.scaled_sensor2_left_limit = center_x + scaled_space 
    self.scaled_sensor2_right_limit = center_x + scaled_space + scaled_width 

    self.right_limit = center_x + scaled_half_x
    self.left_limit = center_x - scaled_half_x

    sensor1_rect_up = pygame.Rect(center_x - scaled_space - scaled_width, center_y - scaled_half_y, scaled_width, scaled_half_y - (scaled_distance / 2))
    sensor1_rect_down = pygame.Rect(center_x - scaled_space - scaled_width, center_y + (scaled_distance / 2), scaled_width, scaled_half_y - (scaled_distance / 2))
    sensor2_rect_up = pygame.Rect(center_x + scaled_space, center_y - scaled_half_y, scaled_width, scaled_half_y - (scaled_distance / 2))
    sensor2_rect_down = pygame.Rect(center_x + scaled_space, center_y  + (scaled_distance / 2), scaled_width, scaled_half_y - (scaled_distance / 2))

    pygame.draw.rect(screen, (0,200,0), sensor1_rect_up)
    pygame.draw.rect(screen, (0,200,0), sensor1_rect_down)
    pygame.draw.rect(screen, (0,200,0), sensor2_rect_up)
    pygame.draw.rect(screen, (0,200,0), sensor2_rect_down)

    pygame.draw.line(screen, (100,100,50), (center_x - scaled_half_x, center_y - (scaled_distance / 2)), (center_x + scaled_half_x, center_y - (scaled_distance / 2)))
    pygame.draw.line(screen, (100,100,50), (center_x - scaled_half_x, center_y + (scaled_distance / 2)), (center_x + scaled_half_x, center_y + (scaled_distance / 2)))

    pygame.draw.line(screen, (255,255,255), (center_x - scaled_half_x, center_y - scaled_half_y), (center_x + scaled_half_x, center_y - scaled_half_y), 7)
    pygame.draw.line(screen, (255,255,255), (center_x + scaled_half_x, center_y - scaled_half_y), (center_x + scaled_half_x, center_y + scaled_half_y), 7)
    pygame.draw.line(screen, (255,255,255), (center_x + scaled_half_x, center_y + scaled_half_y), (center_x - scaled_half_x, center_y + scaled_half_y), 7)
    pygame.draw.line(screen, (255,255,255), (center_x - scaled_half_x, center_y + scaled_half_y), (center_x - scaled_half_x, center_y - scaled_half_y), 7)
    

    return 0 


  def testSensor1(self, partCenter, particle, scale, screen):
    particle_right_limit = particle.pixel_distance + (particle.radius / scale)
    particle_left_limit = particle.pixel_distance - (particle.radius / scale)

    pygame.draw.line(screen, (0,0,0), (particle_left_limit, self.height), (particle_left_limit, 0))
    pygame.draw.line(screen, (0,100,0), (particle_right_limit, self.height), (particle_right_limit, 0))

    pygame.draw.line(screen, (0,0,0), (self.scaled_sensor1_left_limit, self.height), (self.scaled_sensor1_left_limit, 0))
    pygame.draw.line(screen, (0,100,0), (self.scaled_sensor1_right_limit, self.height), (self.scaled_sensor1_right_limit, 0))

    if (particle_right_limit >= self.scaled_sensor1_left_limit and particle_left_limit < self.scaled_sensor1_left_limit):
      if (particle.pixel_distance < self.scaled_sensor1_left_limit):
        height = particle_right_limit - self.scaled_sensor1_left_limit
        volume = ((math.pi * height * height) / 3) * ((3 * (particle.radius / scale)) - height)
      else:
        height = self.scaled_sensor1_left_limit - particle.pixel_distance
        volume = ((math.pi * height * height) / 3) * ((3 * (particle.radius / scale)) - height)
    elif (particle_right_limit <= self.scaled_sensor1_right_limit and particle_left_limit >= self.scaled_sensor1_left_limit):
      volume = particle.volume / scale
    elif (particle_right_limit > self.scaled_sensor1_right_limit and particle_left_limit > self.scaled_sensor1_left_limit and particle_left_limit < self.scaled_sensor1_right_limit):
      if (particle.pixel_distance > self.scaled_sensor1_right_limit):
        height = particle.pixel_distance - self.scaled_sensor1_right_limit
        volume = ((math.pi * height * height) / 3) * ((3 * (particle.radius / scale)) - height)
      else:
        height = self.scaled_sensor1_right_limit - particle_left_limit
        volume = ((math.pi * height * height) / 3) * ((3 * (particle.radius / scale)) - height)
    else:
      volume = 0


    return volume * scale



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
