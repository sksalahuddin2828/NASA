

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Earth parameters
earth_radius = 6371  # Earth radius in kilometers

# Satellite orbit data
num_satellites = 10
inclination_angle = 45  # Orbit inclination angle in degrees

# Generate random semi-major axes and eccentricities for satellite orbits
semi_major_axes = np.random.uniform(800, 1500, num_satellites)
eccentricities = np.random.uniform(0.1, 0.4, num_satellites)

# Time array
num_frames = 100
time = np.linspace(0, 2 * np.pi, num_frames)

# Set up the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the Earth
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 50)
x_earth = earth_radius * np.outer(np.cos(u), np.sin(v))
y_earth = earth_radius * np.outer(np.sin(u), np.sin(v))
z_earth = earth_radius * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_earth, y_earth, z_earth, color='lightblue')

# Plotting the satellite orbits
for i in range(num_satellites):
    semi_major_axis = semi_major_axes[i]
    eccentricity = eccentricities[i]

    # Parametric equations for satellite orbit
    r = semi_major_axis * (1 - eccentricity ** 2) / (1 + eccentricity * np.cos(time))
    x_satellite = r * np.cos(time)
    y_satellite = r * np.sin(time)
    z_satellite = np.zeros_like(x_satellite)

    # Rotate orbit inclination
    angle = np.radians(inclination_angle)
    x_satellite, y_satellite, z_satellite = (
        x_satellite * np.cos(angle) - z_satellite * np.sin(angle),
        y_satellite,
        x_satellite * np.sin(angle) + z_satellite * np.cos(angle)
    )

    # Plot satellite orbit
    ax.plot(x_satellite, y_satellite, z_satellite, color='gray')

# Plotting the invisible red dot satellite
ax.plot([0], [0], [0], marker='o', markersize=8, color='red', alpha=0.0)

# Set plot labels and limits
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.set_title('Satellite Orbits')

# Set plot aspect ratio to be equal
ax.set_box_aspect([1, 1, 1])

plt.show()
