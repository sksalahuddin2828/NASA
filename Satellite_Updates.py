# Please note this: make sure to replace "API_URL_HERE" with the actual URL of the satellite data API and "SATELLITE_DB_API_URL_HERE" with the URL of
# the satellite database API. Additionally, you may need to provide the correct file path for the de421.bsp data file required by the skyfield library.
# Also you need satellite Uplink code -->> Becareful it's a risky code: 

import requests
from skyfield.api import Loader, Topos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Retrieve satellite data from the API
satellite_data_api_url = "API_URL_HERE"
response = requests.get(satellite_data_api_url)
satellite_data = response.json()

# Step 2: Parse TLE data using skyfield
tle_data = []
for satellite in satellite_data:
    line1 = satellite['tle_line1']
    line2 = satellite['tle_line2']
    tle_data.append((line1, line2))

# Load the required data files for calculations
load = Loader('path_to_data_directory')
ephemeris = load('de421.bsp')
satellites = load.tle_file(tle_data)

# Step 3: Visualize satellite orbits in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for satellite in satellites:
    # Calculate the satellite's position over time
    ts = load.timescale()
    t = ts.utc(2023, 7, 11, 0, range(0, 3600, 60))
    geocentric = satellite.at(t)
    subpoint = geocentric.subpoint()

    # Extract latitude, longitude, and altitude
    latitude = subpoint.latitude.degrees
    longitude = subpoint.longitude.degrees
    altitude = subpoint.elevation.km

    # Plot the satellite's trajectory in 3D
    ax.plot(longitude, latitude, altitude)

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Altitude (km)')

# Step 4: Map satellites to countries using the satellite database API
satellite_db_api_url = "SATELLITE_DB_API_URL_HERE"
response = requests.get(satellite_db_api_url)
satellite_db = response.json()

# Mapping satellite names to countries
satellite_country_map = {}
for satellite in satellite_data:
    name = satellite['name']
    for entry in satellite_db:
        if entry['name'] == name:
            country = entry['country']
            satellite_country_map[name] = country
            break

# Printing satellite information
for satellite in satellite_data:
    name = satellite['name']
    angle = satellite['angle']
    country = satellite_country_map.get(name, 'Unknown')

    print(f"Satellite Name: {name}")
    print(f"Orbital Angle: {angle} degrees")
    print(f"Country: {country}")
    print("")

# Show the 3D plot
plt.show()
