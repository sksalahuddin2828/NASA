import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# Earth parameters
earth_radius = 6371  # Earth radius in kilometers
rotation_period = 24  # Earth rotation period in hours

# Satellite orbit data
satellites = [
    {"semi_major_axis": 800, "eccentricity": 0.1, "inclination": 45, "argument_of_periapsis": 0, "ascending_node": 0},
    {"semi_major_axis": 1000, "eccentricity": 0.2, "inclination": 60, "argument_of_periapsis": 0, "ascending_node": 120},
    {"semi_major_axis": 1200, "eccentricity": 0.3, "inclination": 75, "argument_of_periapsis": 0, "ascending_node": 240},
    {"semi_major_axis": 1400, "eccentricity": 0.15, "inclination": 30, "argument_of_periapsis": 0, "ascending_node": 60},
    {"semi_major_axis": 1600, "eccentricity": 0.25, "inclination": 50, "argument_of_periapsis": 0, "ascending_node": 180},
]

# Time array
num_frames = 100
time = np.linspace(0, 2 * np.pi, num_frames)

# Initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Earth surface coordinates
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 50)
x_earth = earth_radius * np.outer(np.cos(u), np.sin(v))
y_earth = earth_radius * np.outer(np.sin(u), np.sin(v))
z_earth = earth_radius * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot Earth surface
earth = ax.plot_surface(x_earth, y_earth, z_earth, color='lightblue', alpha=0.8)

# Initialize satellite lines
satellite_lines = []

# Plotting the satellite orbits
for satellite in satellites:
    semi_major_axis = satellite["semi_major_axis"]
    eccentricity = satellite["eccentricity"]
    inclination = satellite["inclination"]
    argument_of_periapsis = satellite["argument_of_periapsis"]
    ascending_node = satellite["ascending_node"]

    # Parametric equations for satellite orbit
    r = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * np.cos(time))
    x_satellite = r * (np.cos(ascending_node) * np.cos(argument_of_periapsis + time) - np.sin(ascending_node) * np.sin(argument_of_periapsis + time) * np.cos(inclination))
    y_satellite = r * (np.sin(ascending_node) * np.cos(argument_of_periapsis + time) + np.cos(ascending_node) * np.sin(argument_of_periapsis + time) * np.cos(inclination))
    z_satellite = r * (np.sin(argument_of_periapsis + time) * np.sin(inclination))

    # Plot the satellite orbit
    satellite_line, = ax.plot(x_satellite, y_satellite, z_satellite, color='red', linewidth=1)
    satellite_lines.append(satellite_line)

# Animation update function
def update(frame):
    # Rotate Earth around the Z-axis
    angle = (360 / rotation_period) * frame / num_frames
    x_earth_rotated = x_earth * np.cos(np.radians(angle)) - y_earth * np.sin(np.radians(angle))
    y_earth_rotated = x_earth * np.sin(np.radians(angle)) + y_earth * np.cos(np.radians(angle))
    z_earth_rotated = z_earth

    # Update Earth surface plot
    earth._verts3d = x_earth_rotated, y_earth_rotated, z_earth_rotated

    # Update satellite orbits
    for i, satellite_line in enumerate(satellite_lines):
        satellite_line.set_data(x_satellite[:frame+1], y_satellite[:frame+1])
        satellite_line.set_3d_properties(z_satellite[:frame+1])

    return earth, satellite_lines

# Set plot labels and limits
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.set_title('Satellite Orbits')

# Set plot aspect ratio to be equal
ax.set_box_aspect([1, 1, 1])

# Create animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=100)

plt.show()
