import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Satellite orbit data
orbits = [
    {"semi_major_axis": 6780, "eccentricity": 0.001, "inclination": 53, "argument_of_periapsis": 30, "ascending_node": 0},
    {"semi_major_axis": 7160, "eccentricity": 0.003, "inclination": 70, "argument_of_periapsis": 60, "ascending_node": 120},
    {"semi_major_axis": 7000, "eccentricity": 0.002, "inclination": 80, "argument_of_periapsis": 90, "ascending_node": 240},
    {"semi_major_axis": 6500, "eccentricity": 0.0015, "inclination": 45, "argument_of_periapsis": 120, "ascending_node": 60},
    {"semi_major_axis": 6700, "eccentricity": 0.0025, "inclination": 60, "argument_of_periapsis": 150, "ascending_node": 180},
]

# Time array
time = np.linspace(0, 2 * np.pi, 100)

# Plotting the satellite orbits
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for orbit in orbits:
    semi_major_axis = orbit["semi_major_axis"]
    eccentricity = orbit["eccentricity"]
    inclination = orbit["inclination"]
    argument_of_periapsis = orbit["argument_of_periapsis"]
    ascending_node = orbit["ascending_node"]

    # Parametric equations for satellite orbit
    r = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * np.cos(time))
    x = r * (np.cos(ascending_node) * np.cos(argument_of_periapsis + time) - np.sin(ascending_node) * np.sin(argument_of_periapsis + time) * np.cos(inclination))
    y = r * (np.sin(ascending_node) * np.cos(argument_of_periapsis + time) + np.cos(ascending_node) * np.sin(argument_of_periapsis + time) * np.cos(inclination))
    z = r * (np.sin(argument_of_periapsis + time) * np.sin(inclination))

    # Plotting the satellite orbit
    ax.plot(x, y, z)

# Set plot labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Satellite Orbits')
ax.set_xlim3d(-10000, 10000)
ax.set_ylim3d(-10000, 10000)
ax.set_zlim3d(-10000, 10000)

plt.show()
