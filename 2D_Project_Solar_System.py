import math
import pygame

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1800
SUN_RADIUS = 50

# Planet data: name, radius, orbit radius, orbit speed, color, latitude, longitude
PLANETS = [
    ("Mercury", 10, 100, 0.02, (128, 128, 128), 0, 0),       # Gray
    ("Venus", 15, 150, 0.015, (255, 165, 0), 0, 0),          # Orange
    ("Earth", 20, 200, 0.01, (0, 0, 255), 23.5, 0),          # Blue
    ("Mars", 17, 250, 0.008, (255, 0, 0), 25, 0),            # Red
    ("Jupiter", 40, 350, 0.005, (255, 215, 0), 0, 0),        # Gold
    ("Saturn", 35, 450, 0.004, (210, 180, 140), 0, 0),       # Tan
    ("Uranus", 30, 550, 0.003, (0, 255, 255), 0, 0),         # Cyan
    ("Neptune", 30, 650, 0.002, (0, 0, 139), 0, 0),          # Dark Blue
    ("Pluto", 8, 750, 0.001, (165, 42, 42), 0, 0)            # Brown
]

class CelestialBody:
    def __init__(self, name, radius, orbit_radius, orbit_speed, color, latitude, longitude):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.color = color
        self.angle = 0
        self.latitude = latitude
        self.longitude = longitude

    def update(self, dt):
        self.angle += self.orbit_speed * dt

    def get_position(self):
        x = SCREEN_WIDTH // 2 + math.cos(self.angle) * self.orbit_radius
        y = SCREEN_HEIGHT // 2 + math.sin(self.angle) * self.orbit_radius
        return x, y

    def calculate_volume(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        return volume

    def calculate_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return surface_area

    def calculate_orbital_velocity(self):
        orbital_velocity = 2 * math.pi * self.orbit_radius / self.orbit_speed
        return orbital_velocity

    def calculate_gravitational_force(self, other_body):
        distance = math.sqrt((self.latitude - other_body.latitude) ** 2 + (self.longitude - other_body.longitude) ** 2)

    # Check if the distance is zero to avoid division by zero
        if distance == 0:
            return float("inf")  # Return infinity when the distance is zero

        gravitational_force = (6.67430e-11 * self.calculate_mass() * other_body.calculate_mass()) / distance ** 2
        return gravitational_force

    def calculate_mass(self):
        mass = (4 / 3) * math.pi * self.radius ** 3 * 1000  # Assuming density of 1000 kg/m^3
        return mass

def create_celestial_body(name, radius, orbit_radius, orbit_speed, color, latitude, longitude):
    return CelestialBody(name, radius, orbit_radius, orbit_speed, color, latitude, longitude)

def draw_celestial_body(screen, body):
    x, y = body.get_position()

    # Display the name
    name_text = body.name
    name_font = pygame.font.SysFont("Arial", 16)
    name_surface = name_font.render(name_text, True, (255, 255, 255))
    name_rect = name_surface.get_rect(center=(int(x), int(y) + body.radius + 20))
    screen.blit(name_surface, name_rect)

    # Display additional information
    info_text = f"Orbit: {body.orbit_radius}, Latitude: {body.latitude}, Longitude: {body.longitude}"
    info_font = pygame.font.SysFont("Arial", 14)
    info_surface = info_font.render(info_text, True, (255, 255, 255))
    info_rect = info_surface.get_rect(center=(int(x), int(y) + body.radius + 40))
    screen.blit(info_surface, info_rect)

    # Draw the body
    pygame.draw.circle(screen, body.color, (int(x), int(y)), body.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Solar System")

    clock = pygame.time.Clock()

    sun = create_celestial_body("Sun", SUN_RADIUS, 0, 0, (255, 255, 0), 0, 0)
    planets = []

    for planet_data in PLANETS:
        name, radius, orbit_radius, orbit_speed, color, latitude, longitude = planet_data
        planet = create_celestial_body(name, radius, orbit_radius, orbit_speed, color, latitude, longitude)
        planets.append(planet)

    is_running = True

    while is_running:
        dt = clock.tick(60) / 50.0  # Elapsed time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((0, 0, 0))

        for planet in planets:
            planet.update(dt)
            draw_celestial_body(screen, planet)

            # Perform scientific calculations for each planet
            volume = planet.calculate_volume()
            surface_area = planet.calculate_surface_area()
            orbital_velocity = planet.calculate_orbital_velocity()
            gravitational_force = planet.calculate_gravitational_force(sun)

            print(f"Planet: {planet.name}")
            print(f"Volume: {volume}")
            print(f"Surface Area: {surface_area}")
            print(f"Orbital Velocity: {orbital_velocity}")
            print(f"Gravitational Force (with Sun): {gravitational_force}")
            print("-----------------------")

        draw_celestial_body(screen, sun)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
