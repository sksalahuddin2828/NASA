import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation
import warnings

# Suppress warning messages
warnings.filterwarnings("ignore")

# Set up the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)

# Create a Basemap instance
m = Basemap(projection='ortho', lat_0=0, lon_0=0, resolution='l')

# Satellite orbit data
satellites = [
    {"lat": 20, "lon": 40, "radius": 0.2, "color": "red"},
    {"lat": -30, "lon": 120, "radius": 0.15, "color": "blue"},
    {"lat": 40, "lon": -60, "radius": 0.18, "color": "green"},
    {"lat": -50, "lon": 180, "radius": 0.1, "color": "orange"},
    {"lat": 10, "lon": -150, "radius": 0.13, "color": "purple"},
    {"lat": 60, "lon": 30, "radius": 0.17, "color": "cyan"},
    {"lat": -70, "lon": -90, "radius": 0.12, "color": "magenta"},
    {"lat": 0, "lon": 60, "radius": 0.14, "color": "yellow"},
    {"lat": 30, "lon": -120, "radius": 0.16, "color": "lime"},
    {"lat": -20, "lon": 150, "radius": 0.11, "color": "pink"},
]

# Constants for satellite motion
num_frames = 100
orbital_radius = 3.5
angular_speed = 0.05

def update(frame):
    ax.cla()  # Clear the axes
    m = Basemap(projection='ortho', lat_0=0, lon_0=frame, resolution='l')  # Update lon_0 for rotation
    m.drawcoastlines(color='gray')
    m.bluemarble()  # Display the Blue Marble image

    # Update satellite positions
    for satellite in satellites:
        lat = satellite["lat"]
        lon = satellite["lon"]
        radius = satellite["radius"]
        color = satellite["color"]

        # Calculate new position based on orbital motion
        theta = np.radians(frame * angular_speed)
        x = (orbital_radius + radius) * np.cos(theta)
        y = (orbital_radius + radius) * np.sin(theta)

        # Plot satellite position
        m.plot(lon, lat, 'o', markersize=8, color=color, latlon=True)
        m.plot([lon, lon + x], [lat, lat + y], color=color, linewidth=1, latlon=True)

    ax.set_title('3D Earth Rotation and Satellite Orbits')

# Set up the animation with a faster rotation speed (interval=20)
ani = FuncAnimation(fig, update, frames=num_frames, interval=20)

plt.show()
