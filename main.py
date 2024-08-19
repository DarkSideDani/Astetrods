import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # to spawn the player in the middle of the screen
    dt = 0
    
    while True: # This loop keeps the game running. It checks for events (like quitting the game) and will break the loop if the user closes the window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        
        screen.fill("black") # fills the entire screen with the colour black
        player.draw(screen) # rendering the player on the screen
        pygame.display.flip() # updates the screen with everything you’ve drawn during the current frame
        
        dt = clock.tick(60) / 1000.0 # limits the frame rate to 60FPS


if __name__ == "__main__":
    main()