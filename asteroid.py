from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_x = self.position.x
        asteroid_y = self.position.y
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            asteroid_one = Asteroid(asteroid_x, asteroid_y, new_radius)
            asteroid_two = Asteroid(asteroid_x, asteroid_y, new_radius)
            asteroid_one.velocity = vector_one * 1.2
            asteroid_two.velocity = vector_two * 1.2
            


    