import pygame
from constants import LINE_WIDTH


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:

        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def collides_with(self, other) -> bool:
        # distance between the center of two circles
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        # if distance is less than or equal to r1 + r2, collide
        return distance <=(self.radius + other.radius)
