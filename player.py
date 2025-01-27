import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circle import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__ (self,x, y, shots):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots
        self.shot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_timer <= 0:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Create the direction (initial vector facing "up")
        direction = pygame.Vector2(0, 1)  # This assumes 0 degrees points upwards
        # Rotate the vector based on the player's current rotation
        direction = direction.rotate(self.rotation)
        # Scale the vector by PLAYER_SHOOT_SPEED
        velocity = direction * PLAYER_SHOOT_SPEED

        Shot(self.position.x, self.position.y, velocity)

        if self.shot_timer <= 0:
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            new_shot = Shot(self.position.x, self.position.y, velocity)
            self.shots.add(new_shot)  # Add this line

        

