# level 2

#import pygame
import pygame

#import pygame.locals for keyboard controls
from pygame.locals import*

#import assets
import player
import block as block
import key
import door
import button
import gate

#initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()

#create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set background to the Green Sun level 2 background
background = pygame.image.load('level_backdrops/green_sun_l2.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#declare instances of objects
player = player.Player()
player.set_coordinates(player.x, player.y + 10)
block1 = block.Block('images/green_sun_block.png')
block1.set_coordinates(block1.x + 240, block1.y + 12)
key1 = key.Key('images/green_sun_key.png')
key1.set_coordinates(key1.x + 240, key1.y)
door = door.Door('images/green_sun_door.png')
door.set_coordinates(door.x, door.y + 10)
button = button.Button('images/green_sun_button.png')
gate = gate.Gate('images/green_sun_gate.png')

#create variable to keep the game running
running = 1

# create a variable to keep track of whether or not victory message 
# has printed
has_printed = False

while running:
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
    
    # if the player runs into a gate while the button is not on, you
    # cannot move
    if(gate.gate_collide(player, button)):
        if(button.off):
            pass
    
    # if the player runs into a button, well, uh, it keeps going
    if(button.button_collide(player, gate)):
        pass

    # if the player runs into a key, well, uh, it keeps going    
    if(key1.key_collide(player)):
        pass

    # if the player gets to the door and has the key, they win
    if(door.door_collide(player, gate)):
        if(player.has_key):
            if(button.off):
                if(has_printed):
                    print("You win!")
                    has_printed = True
                running = 0
            else:
                if(has_printed):
                    print("You do not win yet.")
                    has_printed = True

    # arrow key and space controls
    player.handle_keys()

    #draw objects
    screen.blit(background,(0,0))
    screen.blit(player.actual, (player.x, player.y))
    screen.blit(block1.actual, (block1.x, block1.y))

    # only blit the button and gate if the player has stepped on it
    if (not button.off):
        screen.blit(button.actual, (button.x, button.y))
    
    screen.blit(gate.actual, (gate.x, gate.y))

    # only blit the key if the player does not have it
    if(not player.has_key):
        screen.blit(key1.actual, (key1.x, key1.y))
    screen.blit(door.actual, (door.x, door.y))
    pygame.display.flip()