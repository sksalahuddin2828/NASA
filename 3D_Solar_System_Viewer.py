import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the solar system data
data = {
    'Name': ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'Type': ['Star', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet'],
    'x': [0, 0.39, 0.72, 1.0, 1.52, 5.20, 9.58, 19.18, 30.07],
    'y': [0, 0, 0, 0, 0, 0, 0, 0, 0],
    'z': [0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Sun
sun = df[df['Name'] == 'Sun']
ax.scatter(sun['x'], sun['y'], sun['z'], s=500, c='yellow', label='Sun')

# Plot the planets
planets = df[df['Type'] == 'Planet']
ax.scatter(planets['x'], planets['y'], planets['z'], s=50, c='blue', label='Planets')

# Set the axis labels
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')

# Set the title
ax.set_title('Solar System')

# Add a legend
ax.legend()

# Show the plot
plt.show()
