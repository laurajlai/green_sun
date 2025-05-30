# level 5

#import pygame
import pygame
import subprocess
import sys

#import pygame.locals for keyboard controls
from pygame.locals import*

#import assets
import player
import portal
from lava import Lava
import flower

#initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()
clock = pygame.time.Clock()

#create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set background to the first Green Sun level 5 background
background = pygame.image.load('level_backdrops/green_sun_l5.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#declare instances of objects used in part 1
player = player.Player()
player.set_coordinates(player.x-80, player.y + 60)
lava1 = Lava('images/green_sun_lava.png')
portal = portal.Portal('images/green_sun_portal.png')
lava2 = Lava('images/green_sun_lava.png')
lava2.set_coordinates(lava1.x + 600, lava1.y)
flower1 = flower.Flower('images/green_sun_flower.png', "horizontal")
flower1.set_coordinates(flower1.x-320, flower1.y-120)
flower2 = flower.Flower('images/green_sun_flower.png', "horizontal")
flower2.set_coordinates(flower1.x+600, flower1.y)

#create variable to keep the game running
running = 1

# create a variable to keep track of whether or not victory message 
# has printed
has_printed = False

# game loop for part 1 of the game
while running == 1:
    #check game events
    for event in pygame.event.get():
        #check to see if the user decided to quit the game
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
        elif event.type == QUIT:
            running = 0

    # if the player runs into lava, the game ends
    if lava1.lava_collide(player) or lava2.lava_collide(player):
        if player.hp <= 0:
            death_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - death_time < 1000:
                screen.blit(player.actual, (player.x, player.y))
                pygame.display.flip()
                clock.tick(60)               
            running = 0
            subprocess.Popen(["python3", 'level5.py'])
            sys.exit()

    # similarly, if the player runs into a flower, keep going
    if(flower1.flower_collide(player) or flower2.flower_collide(player)):
        pass
        
    # if the player gets to the portal, we head to part 2
    if(portal.portal_collide(player, 'level5_p2.py')):
        if(has_printed):
            print("Hold on!")
            has_printed = True
            running = 2
        else:
            if(has_printed):
                print("You do not win yet.")
                has_printed = True

    # arrow key and space controls
    player.handle_keys()
    flower1.move()
    flower2.move()

    #draw the current objects if the portal has not been touched
    if (not portal.activated):
        screen.blit(background,(0,0))
        screen.blit(player.actual, (player.x, player.y))
        screen.blit(lava1.actual, (lava1.x, lava1.y))
        screen.blit(lava2.actual, (lava2.x, lava2.y))
        screen.blit(portal.actual, (portal.x, portal.y))

        # only blit the flower if the player does not have a flower
        if(not flower1.taken):
            screen.blit(flower1.actual, (flower1.x, flower1.y))
        
        if(not flower2.taken):
            screen.blit(flower2.actual, (flower2.x, flower2.y))

    pygame.display.flip()

