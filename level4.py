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
import growshrink
import portal

#initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()

#create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set background to the first Green Sun level 4 background
background = pygame.image.load('level_backdrops/green_sun_l4.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#declare instances of objects used in part 1
player = player.Player()
player.set_coordinates(player.x, player.y + 35)
grow_shrink = growshrink.GrowShrink('images/green_sun_shrink.png', "shrink")
grow_shrink.set_coordinates(grow_shrink.x - 500, grow_shrink.y + 100)
block1 = block.Block('images/green_sun_block.png')
block1.set_coordinates(block1.x + 300, block1.y + 40)
block2 = block.Block('images/green_sun_extralongblock.png')
block2.set_coordinates(block1.x + 100, block1.y-290)
button = button.Button('images/green_sun_button.png')
button.set_coordinates(button.x - 10, button.y + 29)
gate = gate.Gate('images/green_sun_gate.png')
gate.set_coordinates(gate.x-30, gate.y + 29)
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
        running = 0

    # if the player runs into the shrink button, they shrink
    if(grow_shrink.growshrink_collide(player)):
        pass
    
    # if the player runs into the gate with the button on, they can move forwards
    # if the player runs into a gate while the button is not on, you
    # cannot move
    if(gate.gate_collide(player, button)):
        if(button.off):
            pass
    
    # if the player runs into a button, well, uh, it keeps going
    if(button.button_collide(player, gate)):
        pass
        
    # if the player gets to the portal, we head to part 2
    if(portal.portal_collide(player, 'level4_p2.py')):
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

        # gate blitted either way
        screen.blit(gate.actual, (gate.x, gate.y))

        # only blit the shrink module if the player has not used it
        if (not grow_shrink.used):
            screen.blit(grow_shrink.actual, (grow_shrink.x, grow_shrink.y))

    pygame.display.flip()

