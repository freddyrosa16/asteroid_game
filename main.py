import pygame
import sys
from circleshape import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #  Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable) 
    
    # Objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, "black")
        # Restricting our game to draw a maximum of 60 times per second, or 60 FPS.
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        for obj in asteroids:
            for shot in shots:
                if obj.collision(player):
                    print("Game Over!")
                    sys.exit()
                if obj.collision(shot):
                    obj.kill()
                    shot.kill()
                    
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
if __name__ == "__main__":
    main()