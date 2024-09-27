import pygame
import numpy as np
import matplotlib.pyplot as plt
import math
from particle import Particle
from sensor import Sensor
from slider import Slider

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SENSOR_DISTANCE = 200
REST_MEDIUM = 180000

y_lim = 40000
y_lim2 =  0.000000000005 


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

sensor = Sensor(width = 50, distance = SENSOR_DISTANCE, space = 300)
sensor.inputVoltage(5, -5)



silica = Particle(speed = 1, size = 60, perm = 4, rest = pow(10, 12))

time = .1
time_data = []
volume_data = []
sensor_data = []
rest_data = []
current1_data = []
current2_data = []


plt.ion()
fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 10))
line, = ax.plot([], [], 'r-')
line2, = ax.plot([], [], 'g-')
line3, = ax2.plot([], [], 'b-')
line4, = ax2.plot([], [], 'g-')
ax.set_xlim(0, 900)
ax.set_ylim(-0.01, y_lim)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Volume')
ax.set_title('Volume/time')

ax2.set_xlim(0, 900)
ax2.set_ylim(-1 * y_lim2, y_lim2)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Current')
ax2.set_title('Current/time')

slider1 = Slider(20, 20, 100, 20, 20, SENSOR_DISTANCE / 2, 80)
slider2 = Slider(20, 50, 100, 20, .1, 10, 1)
slider3 = Slider(20, 80, 100, 20, 1, 100, 10)

run = True
while run:

  timeScale = slider2.value
  sensor.inputVoltage(slider3.value, -1 * slider3.value)

  distance = silica.move(time)
  if distance > SCREEN_WIDTH + (silica.size * 2):
    time =.1
    time_data = []
    volume_data = []
    sensor_data = []
    rest_data = []
    current1_data = []
    current2_data = []

  screen.fill((0,0,0))

  sensor.generate(SCREEN_WIDTH, SCREEN_HEIGHT, screen)

  pygame.draw.circle(screen, (255, 255, 255), (distance - silica.size, 300), silica.size)
  pygame.draw.circle(screen, (0,255,0), (distance - silica.size, 300), 10)

  slider1.draw(screen)
  slider2.draw(screen)
  slider3.draw(screen)

  silica.updateSize(slider1.value) 

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    slider1.handle_event(event)
    slider2.handle_event(event)
    slider3.handle_event(event)

  volume = sensor.getParticleVolume(distance, silica)
  
  sensor_data_volume = sensor.volume - volume
  sensor_data.append(sensor_data_volume)

  sensor_resistance = REST_MEDIUM * ((pow(sensor.distance, 2) * pow(10, -18)) / (sensor_data_volume * pow(10, -27)))
  nom_sens_res = REST_MEDIUM * ((sensor.distance * pow(10, -9)) / (sensor.width * sensor.distance * pow(10, -18)))

  if volume:  
    particle_resistance = silica.rest * pow((3/(16 * pow(math.pi, 2) * volume * pow(10, -9))), 1/3)
    total_resistance_inv = (1 / particle_resistance) + (1 / sensor_resistance)
  else:
    particle_resistance = 0
    total_resistance_inv = 1 / sensor_resistance
    
  total_resistance = 1 / total_resistance_inv

  current1 = 0  
  current2 = 0
  
  
  which_sensor = sensor.whichSensor(distance, silica)
  if which_sensor == 1:
    current1 = sensor.voltage1 / total_resistance
    current2 = sensor.voltage2 / nom_sens_res
  elif which_sensor == 2:
    current2 = sensor.voltage2 / total_resistance
    current1 = sensor.voltage1 / nom_sens_res
  else:
    current1 = sensor.voltage1 / nom_sens_res
    current2 = sensor.voltage2 / nom_sens_res
    
  current1_data.append(current1)
  current2_data.append(current2)
  print(f"{current1} = {sensor.voltage1} / {total_resistance}")
  rest_data.append(total_resistance)

  if (volume > y_lim):
    y_lim = volume + (volume * 1.2)
    ax.set_ylim(-1000, y_lim)
  
  if (current1 > y_lim2):
    y_lim2 = current1 + (current1 * 1.2)
    ax2.set_ylim(-1 * y_lim2, y_lim2)
  
  

  time_data.append(time)
  volume_data.append(volume)

  line.set_xdata(time_data)
  line.set_ydata(volume_data)
  line2.set_xdata(time_data)
  line2.set_ydata(sensor_data)
  line3.set_xdata(time_data)
  line3.set_ydata(current1_data)
  line4.set_xdata(time_data)
  line4.set_ydata(current2_data)
  ax.relim()
  ax.autoscale_view()
  ax2.relim()
  ax2.autoscale_view()
  plt.draw()
  plt.pause(0.01)

  pygame.display.update()

  time = timeScale + time
  
pygame.quit()


