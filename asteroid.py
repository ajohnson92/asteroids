import pygame
from circle import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)  # make sure velocity is set

    def draw(self, screen):
        if self.alive():  # Only draw if the sprite is still alive
            pygame.draw.circle(screen, (255, 255, 255), (self.position), self.radius, 2)

    def update(self, dt):
        if self.alive():  # Only update if the sprite is still alive
            self.position += self.velocity * dt