# contains logic used in all levels.
import pygame
import subprocess
import sys

# import pygame.locals for keyboard controls
from pygame.locals import*

# initialize screen constants (same for all levels)
WIDTH = 1395
HEIGHT = 677

# initializes pygame, game screen, and game clock
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    return screen, clock

# set backgrounds
def setup_background(background_image):
    background = pygame.image.load(background_image)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    return background

# handles death of a player. after dying, the current level restarts. 
def death_logic(screen, clock, player, level):
    death_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - death_time < 1000:
        screen.blit(player.actual, (player.x, player.y))
        pygame.display.flip()
        clock.tick(60)          
    subprocess.Popen(["python3", level])
    sys.exit()