import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import Scoreboard

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("JK's Asteroids")
    clock = pygame.time.Clock()
    dt = 0
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (updateables, drawables, asteroids)
    AsteroidField.containers = (updateables)
    Shot.containers = (updateables, drawables, shots)
    Scoreboard.containers = (drawables)

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    scoreboard = Scoreboard()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        updateables.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(p1):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.is_colliding(shot):
                    scoreboard.update(asteroid.split())
                    shot.kill()
        pygame.display.flip()

        #60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()