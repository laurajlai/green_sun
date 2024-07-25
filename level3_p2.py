# level 3 

#import pygame
import pygame
import subprocess
import sys

#import pygame.locals for keyboard controls
from pygame.locals import*

#import assets
import player
import block
import key
import door
import flower

#initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()

#create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set background to the second Green Sun level 3 background
background = pygame.image.load('green_sun_l3_p2.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#declare instances of objects used in part 2
player = player.Player()
player.set_coordinates(player.x, player.y + 30)
block1 = block.Block('green_sun_block.png')
block1.set_coordinates(block1.x - 150, block1.y + 33)
longblock1 = block.Block('green_sun_longblock.png')
longblock1.set_coordinates(longblock1.x + 100, longblock1.y-75)
longblock2 = block.Block('green_sun_longblock.png')
longblock2.set_coordinates(longblock1.x + 400, longblock1.y)
flower1 = flower.Flower()
flower2 = flower.Flower()
flower2.set_coordinates(flower1.x + 350, flower1.y)
key = key.Key()
key.set_coordinates(key.x + 420, key.y)
door = door.Door()

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
    if(block1.block_collide(player) or longblock1.block_collide(player) 
    or longblock2.block_collide(player)):
        running = 0

    # if the player runs into a key, well, uh, it keeps going    
    if(key.key_collide(player)):
        pass
    
    # similarly, if the player runs into a flower, keep going
    if(flower1.flower_collide(player) or flower2.flower_collide(player)):
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

    screen.blit(background,(0,0))
    screen.blit(player.actual, (player.x, player.y))
    screen.blit(block1.actual, (block1.x, block1.y))
    screen.blit(longblock1.actual, (longblock1.x, longblock1.y))
    screen.blit(longblock2.actual, (longblock2.x, longblock2.y))

    # only blit the flower if the player does not have a flower
    if(not flower1.taken):
        screen.blit(flower1.actual, (flower1.x, flower1.y))
    
    if(not flower2.taken):
        screen.blit(flower2.actual, (flower2.x, flower2.y))

    # only blit the key and flower if the player does not have it
    if(not player.has_key):
        screen.blit(key.actual, (key.x, key.y))

    pygame.display.flip()

