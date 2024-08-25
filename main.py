import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x, y)
    asteroid_field = AsteroidField()



    while(True):
        for event in pygame.event.get(): # makes the game quit with the x button
            if event.type == pygame.QUIT:
                return
        
        for o in updatable:
            o.update(dt)

        for o in asteroids:
            if o.check_collision(player):
                print("Game over!")
                sys.exit()
            

        pygame.Surface.fill(screen, (0,0,0))
        for o in drawable:
            o.draw(screen)
        pygame.display.flip()
        
        # limits the framerate to 60 fps
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()

    