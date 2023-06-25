import pygame
import math
import time

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1900
SUN_RADIUS = 50

# Planet data: name, radius, orbit radius, orbit speed, color
PLANETS = [
    ("Mercury", 10, 100, 0.02, "gray"),          # Gray
    ("Venus", 15, 150, 0.015, "orange"),         # Orange
    ("Earth", 20, 200, 0.01, "blue"),            # Blue
    ("Mars", 17, 250, 0.008, "red"),             # Red
    ("Jupiter", 40, 350, 0.005, "gold"),         # Gold
    ("Saturn", 35, 450, 0.004, "tan"),           # Tan
    ("Uranus", 30, 550, 0.003, "cyan"),          # Cyan
    ("Neptune", 30, 650, 0.002, "dark blue"),    # Dark Blue
    ("Pluto", 8, 750, 0.001, "brown")            # Brown
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

    def calculate_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def calculate_surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def calculate_orbital_velocity(self):
        return 2 * math.pi * self.orbit_radius / self.orbit_speed

def draw_celestial_body(screen, body, volume, surface_area, orbital_velocity):
    x = SCREEN_WIDTH // 2 + math.cos(body.angle) * body.orbit_radius
    y = SCREEN_HEIGHT // 2 + math.sin(body.angle) * body.orbit_radius

    pygame.draw.circle(screen, body.color, (int(x), int(y)), body.radius)

    font = pygame.font.Font(None, 24)

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

    print(f"{body.name}:")
    print(f"  Volume: {volume:.2f}")
    print(f"  Surface Area: {surface_area:.2f}")
    print(f"  Orbital Velocity: {orbital_velocity:.2f}")
    print()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Celestial Bodies")

    clock = pygame.time.Clock()
    is_running = True

    sun = CelestialBody("Sun", SUN_RADIUS, 0, 0.001, pygame.Color("yellow"))
    planets = []

    for planet_data in PLANETS:
        name, radius, orbit_radius, orbit_speed, color = planet_data
        planet = CelestialBody(name, radius, orbit_radius, orbit_speed, pygame.Color(color))
        planets.append(planet)

    while is_running:
        dt = clock.tick(60) / 50.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((0, 0, 0))

        volume = sun.calculate_volume()
        surface_area = sun.calculate_surface_area()
        orbital_velocity = sun.calculate_orbital_velocity()
        draw_celestial_body(screen, sun, volume, surface_area, orbital_velocity)

        for planet in planets:
            planet.update(dt)
            volume = planet.calculate_volume()
            surface_area = planet.calculate_surface_area()
            orbital_velocity = planet.calculate_orbital_velocity()
            draw_celestial_body(screen, planet, volume, surface_area, orbital_velocity)

        pygame.display.flip()

        time.sleep(0.01)

    pygame.quit()

if __name__ == "__main__":
    main()




#---------------------------------------------------------------------------------------------------------------------------


# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Celestial Bodies")

#     clock = pygame.time.Clock()
#     is_running = True

#     sun = CelestialBody("Sun", SUN_RADIUS, 0, 0, pygame.Color("yellow"))
#     planets = []

#     for planet_data in PLANETS:
#         name, radius, orbit_radius, orbit_speed, color = planet_data
#         planet = CelestialBody(name, radius, orbit_radius, orbit_speed, pygame.Color(color))
#         planets.append(planet)

#     while is_running:
#         dt = clock.tick(60) / 50.0

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 is_running = False

#         screen.fill((0, 0, 0))

#         for planet in planets:
#             planet.update(dt)
#             volume = planet.calculate_volume()
#             surface_area = planet.calculate_surface_area()
#             orbital_velocity = planet.calculate_orbital_velocity()
#             draw_celestial_body(screen, planet, volume, surface_area, orbital_velocity)

#         draw_celestial_body(screen, sun, 0, 0, 0)

#         pygame.display.flip()

#         time.sleep(0.01)

#     pygame.quit()
