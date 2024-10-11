import pygame
import sys
import math

SCREEN_WIDTH = 1352
SCREEN_HEIGHT = 878

scale = 1 * pow(10, -8)

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

  x, y = screen.get_size()

  screen.fill((0,0,105))

  pygame.draw.circle(screen, (150,255,10), (x / 2, y /2), 3 * pow(10, -6) / scale)

  pygame.draw.line(screen, (255,255,255), (x - (x * .1), y - (y * .1)), ((x - (x * .1)) - (1 * pow(10, -6) / scale), y - (y * .1)))

  print((1 *pow(10, -6)) / scale)

  pygame.display.update()

