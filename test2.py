import pygame
import sys
import math
from sensor import Sensor
from particle import Particle
from slider import Slider

SCREEN_WIDTH = 1352
SCREEN_HEIGHT = 878

scale = 1 * pow(10, -8)

sensor = Sensor((50*pow(10, -9)) / scale, (200 * pow(10,-9)) / scale, (300 * pow(10, -9)) / scale)

pygame.init()
pygame.display.set_caption("CytoSim")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

while True:
  # Event handler for pygame 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.VIDEORESIZE:
      screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    if event.type == pygame.MOUSEWHEEL:
      print("SCROLL")
      if event.y == 1:
        scale = scale / 1.1
      elif event.y == -1:
        scale = scale * 1.1

  x, y = screen.get_size()

  screen.fill((200,100,5))

  sensor.generate(x, y, screen)

  pygame.draw.circle(screen, (150,255,10), (x / 2, y /2), 3 * pow(10, -6) / scale)

  pygame.draw.line(screen, (255,255,255), (x - (x * .1), y - (y * .1)), ((x - (x * .1)) - (1 * pow(10, -6) / scale), y - (y * .1)))

  print(scale)
  #print((1 *pow(10, -6)) / scale)

  pygame.display.update()

