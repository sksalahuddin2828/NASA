import ephem
import numpy as np
from mayavi import mlab

# Read TLE data from a file
tle_file = "tle_data.txt"  # Path to the TLE file
tle_data = []
with open(tle_file, "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        line1 = lines[i+1].strip()
        line2 = lines[i+2].strip()
        tle_data.append((name, line1, line2))

# Satellite names and colors for plotting
satellite_names = ["ISS (ZARYA)", "Hubble", "GPS IIR-10", "Terra", "Aqua"]
satellite_colors = ["yellow", "cyan", "magenta", "green", "red"]

# Set up the MayaVi figure
fig = mlab.figure(size=(800, 600), bgcolor=(0, 0, 0))

# Initialize the Earth and satellite paths
earth = mlab.points3d(0, 0, 0, color=(0, 0, 1), scale_factor=1)
satellites = []

# Compute satellite positions and plot their orbits
for i, (name, line1, line2) in enumerate(tle_data):
    sat = ephem.readtle(name, line1, line2)
    sat_positions = []
    for j in range(0, 360, 5):
        sat.compute(f"2023/7/11 {j}:00:00")
        sat_positions.append((sat.sublong, sat.sublat, sat.elevation / 1000.0))  # Divide elevation by 1000 for scaling

    sat_positions = np.array(sat_positions)
    satellite = mlab.plot3d(sat_positions[:, 0], sat_positions[:, 1], sat_positions[:, 2], tube_radius=0.2,
                            color=satellite_colors[i], name=name)
    satellites.append(satellite)

    # Label each satellite
    mlab.text3d(sat_positions[-1, 0], sat_positions[-1, 1], sat_positions[-1, 2], name, color=satellite_colors[i])

# Set up the visualization parameters
mlab.view(azimuth=0, elevation=90, distance=8, focalpoint=(0, 0, 0))
mlab.xlabel("X")
mlab.ylabel("Y")
mlab.zlabel("Z")
mlab.title("Satellite Orbits")

# Animate the visualization
@mlab.animate(delay=100)
def animate():
    while True:
        for satellite in satellites:
            satellite.mlab_source.trait_set(x=satellite.mlab_source.x[1:], y=satellite.mlab_source.y[1:], z=satellite.mlab_source.z[1:])
        yield

# Start the animation
animate()

# Display the visualization
mlab.show()
