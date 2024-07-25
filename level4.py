# level 4

#import pygame
import pygame

#import pygame.locals for keyboard controls
from pygame.locals import*

#import assets
import player
import block
import button
import gate
import portal

#initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()

#create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set background to the first Green Sun level 4 background
background = pygame.image.load('green_sun_l4.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#declare instances of objects used in part 1
player = player.Player()
player.set_coordinates(player.x, player.y + 35)
block1 = block.Block('green_sun_block.png')
block1.set_coordinates(block1.x + 100, block1.y + 40)
block2 = block.Block('green_sun_extralongblock.png')
block2.set_coordinates(block1.x + 100, block1.y-250)
button = button.Button()
button.set_coordinates(button.x - 10, button.y + 29)
gate = gate.Gate()
gate.set_coordinates(gate.x-30, gate.y + 29)
portal = portal.Portal()

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
    if(block1.block_collide(player)):
        running = 0

    # if the player gets to the portal, we head to part 2
    if(portal.portal_collide(player, 'level3_p2.py')):
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

        # only blit the button and gate if the player has stepped on it
        if (not button.off):
            screen.blit(button.actual, (button.x, button.y))

        screen.blit(gate.actual, (gate.x, gate.y))

    pygame.display.flip()

