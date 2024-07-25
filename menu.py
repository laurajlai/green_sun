# main menu

# import pygame and subprocess
import pygame
import subprocess

# import pygame.locals for keyboard controls
from pygame.locals import*

# initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()

# create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set background to the Green Sun menu
background = pygame.image.load('green_sun_menu.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# class for clickable buttons (play, levels, quit, etc.)
# a clickable button uses exec to redirect to another page.
class ClickButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('green_sun_playbutton.png').convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.6), int(self.size[1]*0.6)))

        # play button coordinates, rectangle
        self.x = 650
        self.y = 300
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))
    
    # changes the coordinates of a ClickButton object
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

# declare instances of assets used in the menu
play_button = ClickButton()
# create variable to keep the game running
running = 1

# create a variable to keep track of whether or not victory message 
# has printed
has_printed = False

while running:
    # check game events
    for event in pygame.event.get():
        # check to see if the user decided to quit the game or restart
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
            elif event.key == pygame.K_r:
                main()
        # check to see if you clicked the play button
        # if you clicked the play button, start level 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    subprocess.Popen(["python3", "level1.py"])
                    pygame.quit()
                    running = 0
        elif event.type == QUIT:
            running = 0

    if running != 0:
        screen.blit(background,(0,0))
        screen.blit(play_button.actual, (play_button.x, play_button.y))
        pygame.display.flip()

pygame.quit()