# level 1

# import pygame
import pygame
import os

# import pygame.locals for keyboard controls
from pygame.locals import*

# import assets
import player
import block as block
import key
import door

# initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()

# create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set background to the Green Sun level 1 background
background = pygame.image.load('level_backdrops/green_sun_l1.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# declare instances of objects
player = player.Player()
block1 = block.Block('images/green_sun_block.png')
block2 = block.Block('images/green_sun_block.png')
key1 = key.Key('images/green_sun_key.png')
door = door.Door('images/green_sun_door.png')

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
        elif event.type == QUIT:
            running = 0

    # if the player runs into a block, the game ends
    if(block1.block_collide(player)):
        running = 0

    if(block2.block_collide(player)):
        running = 0

    # if the player runs into a key, well, uh, it keeps going    
    if(key1.key_collide(player)):
        pass

    # if the player gets to the door and has the key, they win
    if(door.door_collide(player)):
        if(player.has_key):
            if(has_printed):
                print("You win!")
                has_printed = True
            running = 0

    # arrow key and space controls
    player.handle_keys()

    # draw objects
    screen.blit(background,(0,0))
    screen.blit(player.actual, (player.x, player.y))
    screen.blit(block1.actual, (block1.x, block1.y))
    block2.set_coordinates(block1.x + 300, block1.y)
    screen.blit(block2.actual, (block2.x, block2.y))

    # only blit the key if the player does not have it
    if(not player.has_key):
        screen.blit(key1.actual, (key1.x, key1.y))
    screen.blit(door.actual, (door.x, door.y))
    pygame.display.flip()