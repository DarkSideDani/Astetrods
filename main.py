# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True: # This loop keeps the game running. It checks for events (like quitting the game) and will break the loop if the user closes the window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black") # fills the entire screen with the colour black
        pygame.display.flip() # updates the screen with everything you’ve drawn during the current frame
        


if __name__ == "__main__":
    main()