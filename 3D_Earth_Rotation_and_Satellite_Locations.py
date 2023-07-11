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
    {"lat": 20, "lon": 40},
    {"lat": -30, "lon": 120},
    {"lat": 40, "lon": -60},
    {"lat": -50, "lon": 180},
    {"lat": 10, "lon": -150},
    {"lat": 60, "lon": 30},
    {"lat": -70, "lon": -90},
    {"lat": 0, "lon": 60},
    {"lat": 30, "lon": -120},
    {"lat": -20, "lon": 150},
]

def update(frame):
    ax.cla()  # Clear the axes
    m = Basemap(projection='ortho', lat_0=0, lon_0=frame, resolution='l')  # Update lon_0 for rotation
    m.drawcoastlines(color='gray')
    m.bluemarble()  # Display the Blue Marble image

    # Plotting satellite positions
    for satellite in satellites:
        lat = satellite["lat"]
        lon = satellite["lon"]
        x, y = m(lon, lat)
        m.plot(x, y, 'ro', markersize=5, latlon=False)

    ax.set_title('3D Earth Rotation and Satellite Locations')

# Set up the animation with a faster rotation speed (interval=20)
ani = FuncAnimation(fig, update, frames=range(0, 360, 2), interval=20)
plt.show()
