# The TLE data for the five satellites is provided in the tle_data list. The satellite_names list holds
# the names of the satellites, and satellite_colors determines the colors used for plotting each satellite's orbit.

# The code uses the mayavi.mlab module to create the 3D plot and mlab.animate to animate the orbits.
# The satellite positions are computed for each time step and plotted as 3D paths.
    
import ephem
import numpy as np
from mayavi import mlab

# Satellite TLE data
tle_data = [
    ("ISS (ZARYA)",
     "1 25544U 98067A   21186.47390511  .00000500  00000-0  13696-4 0  9994",
     "2 25544  51.6431 283.7920 0009298 204.6780 155.3723 15.49061430341806"),
    ("Hubble Space Telescope",
     "1 20580U 90037B   21187.51485065  .00000700  00000-0  26089-4 0  9992",
     "2 20580  28.4693 132.2321 0001726 352.6060   7.4753 15.09123027248244"),
    ("GPS IIR-10 (M)",
     "1 30793U 07015M   21186.29253259 -.00000037  00000-0  00000-0 0  9999",
     "2 30793  56.1985  60.4463 0064704 249.4686 109.0947  2.00567978134673"),
    ("Terra",
     "1 25994U 99068A   21187.36675641  .00000052  00000-0  12124-4 0  9992",
     "2 25994  98.2025 202.0731 0001307  86.8101 273.3496 14.57198865489823"),
    ("Aqua",
     "1 27424U 02022A   21187.42292448  .00000100  00000-0  98692-4 0  9999",
     "2 27424  98.2027 189.4386 0001339  88.5354 271.6320 14.57198322495156")
]

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


#------------------------------------------------------------arduino---------------------------------------------------------------------


# ("ISS (ZARYA)",
#  "1 25544U 98067A   21186.47390511  .00000500  00000-0  13696-4 0  9994",
#  "2 25544  51.6431 283.7920 0009298 204.6780 155.3723 15.49061430341806")
