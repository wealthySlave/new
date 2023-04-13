import sys
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Tank properties
tank_speed = 1
angular_velocity = np.radians(10)
resistance_factor = 0.05

# Create the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tank Simulation")

# Load tank image
tank_image = pygame.image.load(
  "tank.png")  # Replace "tank.png" with your tank image file

# Tank initial position and direction
position = np.array([screen_width // 2, screen_height // 2], dtype=float)
direction = 0


def resistance_gradient(position):
  return position[0] / screen_width * resistance_factor


def update_tank_position(position, direction, tank_speed):
  resistance = resistance_gradient(position)
  delta_position = tank_speed * np.array(
    [np.cos(direction), np.sin(direction)]) * (1 - resistance)
  new_position = position + delta_position
  new_direction = direction + angular_velocity
  return new_position, new_direction


clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Update tank position and direction
  position, direction = update_tank_position(position, direction, tank_speed)

  # Clear the screen
  screen.fill((255, 255, 255))

  # Draw the tank
  rotated_tank = pygame.transform.rotate(tank_image, -np.degrees(direction))
  rect = rotated_tank.get_rect(center=(position[0], position[1]))
  screen.blit(rotated_tank, rect.topleft)

  # Update the display
  pygame.display.flip()

  # Cap the frame rate
  clock.tick(60)
