import sys
import pygame
from pygame.time import Clock
from asteroid import Asteroid
from asteroidfield import AsteroidField
import asteroidfield
from logger import log_state, log_event
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}"
    )

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #1. player actions update
        updatable.update(dt)

        #2. Check collision
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)

        #2. draw objects on screen
        for obj in drawable:
            obj.draw(screen)

        #3. Push the complete frame (render)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
