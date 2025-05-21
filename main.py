import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    dt = 0
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        # Restricting our game to draw a maximum of 60 times per second, or 60 FPS.
        clock.tick(60)
        dt = clock.tick(60) / 1000
        
        # Giving color to our GUI
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        player.draw(screen)
        

if __name__ == "__main__":
    main()