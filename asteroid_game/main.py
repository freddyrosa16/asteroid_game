from constants import *
from player import Player
from circleshape import CircleShape
import pygame

def main():
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        pygame.Surface.fill(screen, "black")

        for obj in drawable:
            obj.draw(screen) 

        
        pygame.display.flip()
        dt = pygame.time.Clock.tick(clock, 60) / 1000


if __name__ == "__main__":
    main()
