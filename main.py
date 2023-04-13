import numpy as np
import matplotlib.pyplot as plt

def resistance_gradient(position):
    return position[0] * resistance_factor

def update_tank_position(position, direction, speed):
    resistance = resistance_gradient(position)
    delta_position = speed * np.array([np.cos(direction), np.sin(direction)]) * (1 - resistance)
    new_position = position + delta_position
    new_direction = direction + angular_velocity
    return new_position, new_direction

# Initial conditions
initial_position = np.array([0, 0])
initial_direction = 0
speed = 1
angular_velocity = np.radians(10)
resistance_factor = 0.05
time_steps = 1000

# Run the simulation
position = initial_position
direction = initial_direction
positions = [initial_position]

for t in range(time_steps):
    position, direction = update_tank_position(position, direction, speed)
    positions.append(position)

# Visualize the results
positions = np.array(positions)
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Tank's Path with Resistance Gradient")
plt.show()
