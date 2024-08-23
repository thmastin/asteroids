# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = updateable, drawable  
    Asteroid.containers = updateable, drawable, asteroids
    AsteroidField.containers = updateable
    Shot.containers = updateable, drawable, shots

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field_instance = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)
        for thing in updateable:
            thing.update(dt)
        for thing in asteroids:
            if thing.is_colliding_with_another_circle_shape(player):
                print("Game Over!")
                exit()
        for thing in asteroids:
            for shot in shots:
                if thing.is_colliding_with_another_circle_shape(shot):
                    thing.split()
                    shot.kill()
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        

        
        #print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()