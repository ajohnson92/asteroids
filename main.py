import pygame
from pygame.math import Vector2
import sys
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots)
    asteroid_field = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    while True:
        dt = clock.tick(60) / 1000
    
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Clear screen
        screen.fill((0, 0, 0))
    
        # Update game state
        updatable.update(dt)
        # Check collisions
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.alive() and shot.alive():
                    distance = (shot.position - asteroid.position).length()
                    if distance < (asteroid.radius + shot.radius):
                        if asteroid.radius > 30:
                            shot.kill()
                            asteroid.kill()
                            pos = asteroid.position
                            orig_velocity = asteroid.velocity
                            new_asteroid1 = Asteroid(pos.x, pos.y, radius=20)
                            new_asteroid2 = Asteroid(pos.x, pos.y, radius=20)
        
                            new_asteroid1.velocity = orig_velocity + pygame.Vector2(-5, -3)
                            new_asteroid2.velocity = orig_velocity + pygame.Vector2(5, 2)
        
                            asteroids.add(new_asteroid1)
                            asteroids.add(new_asteroid2)
                        elif asteroid.radius > 15:
                            shot.kill()
                            asteroid.kill()
                            pos = asteroid.position
                            orig_velocity = asteroid.velocity
                            new_asteroid1 = Asteroid(pos.x, pos.y, radius=8)
                            new_asteroid2 = Asteroid(pos.x, pos.y, radius=8)
        
                            new_asteroid1.velocity = orig_velocity + pygame.Vector2(-5, -3)
                            new_asteroid2.velocity = orig_velocity + pygame.Vector2(5, 2)
        
                            asteroids.add(new_asteroid1)
                            asteroids.add(new_asteroid2)
                        elif asteroid.radius <= 15:
                            shot.kill()
                            asteroid.kill()
                            asteroids.remove(asteroid)
                            updatable.remove(asteroid)
                            drawable.remove(asteroid)

        # Draw everything (only once!)
        for sprite in drawable:
            sprite.draw(screen)
    
        # Flip display
        pygame.display.flip()

if __name__ == "__main__":
        main()