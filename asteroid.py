import pygame
from constants import *
from circleshape import CircleShape
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
        
    def split(self):
        # Asteroid always dies
        self.kill()
        # if smallest asteroids, do nothing else
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        
        first = self.velocity.rotate(angle)
        second = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        
        first_asteroid.velocity = first
        second_asteroid.velocity = second