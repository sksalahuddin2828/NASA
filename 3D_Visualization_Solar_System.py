import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the coordinates and sizes of the celestial bodies
bodies = {
    "Sun": (0, 0, 0, 20),
    "Mercury": (50, 0, 0, 5),
    "Venus": (70, 0, 0, 7),
    "Earth": (100, 0, 0, 7),
    "Mars": (150, 0, 0, 6),
    "Jupiter": (220, 0, 0, 18),
    "Saturn": (280, 0, 0, 15),
    "Uranus": (350, 0, 0, 12),
    "Neptune": (400, 0, 0, 12),
}

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot each body as a sphere
for body, (x, y, z, size) in bodies.items():
    ax.scatter(x, y, z, s=size, label=body)

# Set the aspect ratio and labels
ax.set_box_aspect([1, 1, 1])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Add a legend
ax.legend()

# Show the plot
plt.show()
