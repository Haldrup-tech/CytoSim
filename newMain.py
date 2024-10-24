
import pygame
import sys
import math
from sensor import Sensor
from particle import Particle
from slider import Slider

SCREEN_WIDTH = 1352
SCREEN_HEIGHT = 878

scale = 1 * pow(10, -6)
unit_scale = -3

sensor = Sensor( 50 * pow(10, -6), 30 * pow(10, -6),  20 * pow(10, -6))

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
    if event.type == pygame.KEYDOWN:
      print("Button")
      if event.key == pygame.K_UP:
        scale = scale / 1.1
      elif event.key == pygame.K_DOWN:
        scale = scale * 1.1


  x, y = screen.get_size()

  scale_bar_size = abs((x - (x * .1)) - (x - (x * .1)) - (1 * pow(10, unit_scale) / scale))

  print(scale_bar_size)
  if int(scale_bar_size) < 40:
    unit_scale += 1
  elif int(scale_bar_size) > 100:
    unit_scale -= 1

  scale_bar_end_point = (x - (x * .1)) - (1 * pow(10, unit_scale) / scale)

  screen.fill((200,100,5))

  sensor.display(x, y, screen, scale)

  pygame.draw.circle(screen, (150,255,10), (x / 2, y /2), 3 * pow(10, -6) / scale)

  pygame.draw.line(screen, (255,255,255), (x - (x * .1), y - (y * .1)), (scale_bar_end_point, y - (y * .1)))

  print(scale)
  #print((1 *pow(10, -6)) / scale)

  pygame.display.update()
