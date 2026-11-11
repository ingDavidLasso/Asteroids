import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
           return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            positive_velocity = self.velocity.rotate(angle)
            negative_velocity = self.velocity.rotate(-angle)
            old_radius = self.radius

            new_radius = old_radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_one.velocity = positive_velocity * 1.2
            asteroid_two.velocity = negative_velocity * 1.2
