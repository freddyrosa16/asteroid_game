import pygame
from constants import *
from player import *

def main():
    pygame.init()
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    #  Containers
    Player.containers = (updatable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
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
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
if __name__ == "__main__":
    main()