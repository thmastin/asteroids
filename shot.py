from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = SHOT_RADIUS
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
