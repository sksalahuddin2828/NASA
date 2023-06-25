import math
import pygame

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1900

SUN_RADIUS = 50

# Planet data: name, radius, orbit radius, orbit speed, color
PLANETS = [
    ("Mercury", 10, 100, 0.02, (128, 128, 128)),
    ("Venus", 15, 150, 0.015, (255, 165, 0)),
    ("Earth", 20, 200, 0.01, (0, 0, 255)),
    ("Mars", 17, 250, 0.008, (255, 0, 0)),
    ("Jupiter", 40, 350, 0.005, (255, 215, 0)),
    ("Saturn", 35, 450, 0.004, (210, 180, 140)),
    ("Uranus", 30, 550, 0.003, (0, 255, 255)),
    ("Neptune", 30, 650, 0.002, (0, 0, 139)),
    ("Pluto", 8, 750, 0.001, (165, 42, 42))
]

class CelestialBody:
    def __init__(self, name, radius, orbit_radius, orbit_speed, color):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.color = color
        self.angle = 0

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
        if self.orbit_speed == 0:
            return float('inf')
        orbital_velocity = 2 * math.pi * self.orbit_radius / self.orbit_speed
        return orbital_velocity

def create_celestial_body(name, radius, orbit_radius, orbit_speed, color):
    return CelestialBody(name, radius, orbit_radius, orbit_speed, color)

def draw_celestial_body(screen, body):
    x, y = body.get_position()

    # Perform scientific calculations for each planet
    volume = body.calculate_volume()
    surface_area = body.calculate_surface_area()
    orbital_velocity = body.calculate_orbital_velocity()

    # Print calculations to console
    print("Scientific Calculations:")
    print(f"Planet: {body.name}")
    print(f"Volume: {volume:.2f}")
    print(f"Surface Area: {surface_area:.2f}")
    print(f"Orbital Velocity: {orbital_velocity:.2f}")
    print("------------------------")

    # Render the calculations as text on the screen
    font = pygame.font.SysFont("Arial", 16)
    volume_text = f"Volume: {volume:.2f}"
    volume_surface = font.render(volume_text, True, (255, 255, 255))
    volume_rect = volume_surface.get_rect(center=(int(x), int(y) + body.radius + 20))
    screen.blit(volume_surface, volume_rect)

    surface_area_text = f"Surface Area: {surface_area:.2f}"
    surface_area_surface = font.render(surface_area_text, True, (255, 255, 255))
    surface_area_rect = surface_area_surface.get_rect(center=(int(x), int(y) + body.radius + 40))
    screen.blit(surface_area_surface, surface_area_rect)

    orbital_velocity_text = f"Orbital Velocity: {orbital_velocity:.2f}"
    orbital_velocity_surface = font.render(orbital_velocity_text, True, (255, 255, 255))
    orbital_velocity_rect = orbital_velocity_surface.get_rect(center=(int(x), int(y) + body.radius + 60))
    screen.blit(orbital_velocity_surface, orbital_velocity_rect)

    # Draw the body
    pygame.draw.circle(screen, body.color, (int(x), int(y)), body.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Planetary System")
    clock = pygame.time.Clock()

    sun = create_celestial_body("Sun", SUN_RADIUS, 0, 0, (255, 255, 0))
    planets = []

    for planet_data in PLANETS:
        name, radius, orbit_radius, orbit_speed, color = planet_data
        planet = create_celestial_body(name, radius, orbit_radius, orbit_speed, color)
        planets.append(planet)

    is_running = True

    while is_running:
        dt = clock.tick(60) / 50.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((0, 0, 0))

        for planet in planets:
            planet.update(dt)
            draw_celestial_body(screen, planet)

        draw_celestial_body(screen, sun)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
