import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, circle_shape):
        distance = self.position.distance_to(circle_shape.position)
        return distance <= self.radius + circle_shape.radius
    
    def wrap_screen(self):
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -1 * self.radius
        if self.position.x < -1 * self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -1 * self.radius
        if self.position.y < -1 * self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius