# level 3 

#import pygame
import pygame
import subprocess
import sys

#import pygame.locals for keyboard controls
from pygame.locals import*

#import assets
import player
import block as block
import key
import portal

#initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()
clock = pygame.time.Clock()

#create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set background to the first Green Sun level 3 background
background = pygame.image.load('level_backdrops/green_sun_l3.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#declare instances of objects used in part 1
player = player.Player()
player.set_coordinates(player.x, player.y + 20)
block1 = block.Block('images/green_sun_block.png')
block1.set_coordinates(block1.x + 100, block1.y + 24)
block2 = block.Block('images/green_sun_block.png')
block2.set_coordinates(block1.x + 400, block1.y)
key1 = key.Key('images/green_sun_key.png')
key1.set_coordinates(key1.x + 150, key1.y)
portal = portal.Portal('images/green_sun_portal.png')

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

    # if the player runs into a block, the game ends
    if(block1.block_collide(player) or block2.block_collide(player)):
        death_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - death_time < 1000:
            screen.blit(player.actual, (player.x, player.y))
            pygame.display.flip()
            clock.tick(60)       
        
        running = 0
        subprocess.Popen(["python3", 'level3.py'])
        sys.exit()

    # if the player runs into a key, well, uh, it keeps going    
    if(key1.key_collide(player) and not portal.activated):
        pass

    # if the player gets to the portal, we head to part 2
    if(portal.portal_collide(player, 'level3_p2.py')):
        if(player.has_key):
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

    #draw the current objects if the portal has not been touched
    if (not portal.activated):
        screen.blit(background,(0,0))
        screen.blit(player.actual, (player.x, player.y))
        screen.blit(block1.actual, (block1.x, block1.y))
        screen.blit(block2.actual, (block2.x, block2.y))
        screen.blit(portal.actual, (portal.x, portal.y))

        # only blit the key if the player does not have it
        if(not player.has_key):
            screen.blit(key1.actual, (key1.x, key1.y))

    pygame.display.flip()

