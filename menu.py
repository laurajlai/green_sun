# main menu

# import pygame and subprocess
import pygame
import clickbutton

# import pygame.locals for keyboard controls
from pygame.locals import*

# initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()

# create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set background to the Green Sun menu
background = pygame.image.load('level_backdrops/green_sun_menu.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# declare instances of assets used in the menu
play_button = clickbutton.ClickButton("green_sun_playbutton.png", "play")
levels_button = clickbutton.ClickButton("green_sun_levelsbutton.png", "level")
levels_button.set_coordinates(play_button.x, play_button.y + 120)
# create variable to keep the game running
running = 1

# create a variable to keep track of whether or not victory message 
# has printed
has_printed = False

while running:
    if running != 0:  # Only render if the game is still running
        screen.blit(background, (0, 0))
        screen.blit(play_button.actual, (play_button.x, play_button.y))
        screen.blit(levels_button.actual, (levels_button.x, levels_button.y))
        pygame.display.flip()
        for event in pygame.event.get():
            # Handle quit events
            if event.type == QUIT:  # User closed the window
                running = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # User pressed Escape
                    running = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.clicked():  # Play button clicked
                    pygame.quit()
                    break


