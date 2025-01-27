import pygame
from circle import CircleShape


class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__ (self, x, y, velocity):
        super().__init__(x, y, Shot.SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),  # White color
            (int(self.position.x), int(self.position.y)),  # Round position to integers
            self.SHOT_RADIUS
        )
    def update(self, dt):
        self.position += self.velocity * dt