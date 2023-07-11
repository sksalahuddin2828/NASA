import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Earth parameters
earth_radius = 6371  # Earth radius in kilometers

# Satellite parameters
num_satellites = 10
satellite_radius = 100  # Satellite radius in kilometers
satellite_color = 'red'

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

# Plotting the satellite orbits and markers
for i in range(num_satellites):
    semi_major_axis = semi_major_axes[i]
    eccentricity = eccentricities[i]

    # Parametric equations for satellite orbit
    r = semi_major_axis * (1 - eccentricity ** 2) / (1 + eccentricity * np.cos(time))
    x_satellite = r * np.cos(time)
    y_satellite = r * np.sin(time)
    z_satellite = np.zeros_like(x_satellite)

    # Plot satellite orbit
    ax.plot(x_satellite, y_satellite, z_satellite, color='gray')

    # Plotting the satellite markers
    marker_x = x_satellite[-1]
    marker_y = y_satellite[-1]
    marker_z = z_satellite[-1]
    ax.scatter(marker_x, marker_y, marker_z, color=satellite_color, s=satellite_radius, alpha=0.8)

# Set plot labels and limits
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.set_title('Satellite Orbits')

# Set plot aspect ratio to be equal
ax.set_box_aspect([1, 1, 1])

plt.show()
