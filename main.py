# this allows us to use code from
# the open source pygame library
# throughout this file

import pygame
from constants import *
from player import *

pygame.init()

clock = pygame.time.Clock()

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill((0, 0, 0))
        for thing in updateable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()