import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    while True: # This loop keeps the game running. It checks for events (like quitting the game) and will break the loop if the user closes the window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000 # limits the frame rate to 60FPS
        
        for obj in updatable:
            obj.update(dt)
        
        screen.fill("black") # fills the entire screen with the colour black
        
        for obj in drawable:
            obj.draw(screen)# rendering the player on the screen
        
        pygame.display.flip() # updates the screen with everything you’ve drawn during the current frame


if __name__ == "__main__":
    main()